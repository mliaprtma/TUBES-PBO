from flask import Flask, render_template, request, redirect, session
from koneksi import db

app = Flask(__name__)
app.secret_key = "simobs_admin"


# =========================
# HOME
# =========================

@app.route('/')
def home():
    return redirect('/login')


# =========================
# REGISTER
# =========================

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        nama = request.form['nama']
        username = request.form['username']
        password = request.form['password']

        cek = db.collection("admins").where("username", "==", username).stream()
        if list(cek):
            error = "Username sudah digunakan"
            return render_template('register.html', error=error)

        db.collection("admins").add({
            "nama": nama,
            "username": username,
            "password": password
        })
        return redirect('/login')

    return render_template('register.html', error=error)


# =========================
# LOGIN
# =========================

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        docs = db.collection("admins").where("username", "==", username).where("password", "==", password).stream()
        admin = None
        for doc in docs:
            admin = doc.to_dict()
            break

        if admin:
            session['admin'] = admin['username']
            session['nama'] = admin['nama']
            session['username'] = admin['username']
            return redirect('/dashboard')

        error = "Username atau Password Salah"

    return render_template('login.html', error=error)


# profile
@app.route('/profil')
def profil():
    return redirect('/dashboard')


# =========================
# DASHBOARD
# =========================

@app.route('/dashboard')
def dashboard():
    if 'admin' not in session:
        return redirect('/login')

    # Menghitung jumlah dokumen di setiap koleksi Firestore
    total_pelanggan = len(db.collection("pelanggan").get())
    total_booking = len(db.collection("booking").get())
    total_sparepart = len(db.collection("sparepart").get())
    total_admin = len(db.collection("admins").get())
    total_cs = len(db.collection("customer_service").get())

    return render_template(
        'dashboard.html',
        admin=session.get('admin', ''),
        nama=session.get('nama', ''),
        username=session.get('username', ''),
        pelanggan=total_pelanggan,
        booking=total_booking,
        sparepart=total_sparepart,
        total_admin=total_admin,
        total_cs=total_cs
    )


# =========================
# PELANGGAN
# =========================

@app.route('/pelanggan')
def pelanggan():
    if 'admin' not in session:
        return redirect('/login')

    keyword = request.args.get('keyword', '')
    docs = db.collection("pelanggan").stream()
    data = []

    for doc in docs:
        item = doc.to_dict()
        nama = item.get("nama", "")
        alamat = item.get("alamat", "")
        telepon = item.get("telepon", "")

        if keyword:
            text = f"{nama} {alamat} {telepon}".lower()
            if keyword.lower() not in text:
                continue

        data.append({
            "id": doc.id,
            "nama": nama,
            "alamat": alamat,
            "telepon": telepon
        })

    return render_template('pelanggan.html', data=data, keyword=keyword)


@app.route('/tambah_pelanggan', methods=['GET', 'POST'])
def tambah_pelanggan():
    if request.method == 'POST':
        db.collection("pelanggan").add({
            "nama": request.form['nama'],
            "alamat": request.form['alamat'],
            "telepon": request.form['telepon']
        })
        return redirect('/pelanggan')
    return render_template('tambah_pelanggan.html')


@app.route('/edit_pelanggan/<id>', methods=['GET', 'POST'])
def edit_pelanggan(id):
    doc_ref = db.collection("pelanggan").document(id)
    
    if request.method == 'POST':
        doc_ref.update({
            "nama": request.form['nama'],
            "alamat": request.form['alamat'],
            "telepon": request.form['telepon']
        })
        return redirect('/pelanggan')

    data = doc_ref.get().to_dict()
    data['id'] = id
    return render_template('edit_pelanggan.html', data=data)


@app.route('/hapus_pelanggan/<id>')
def hapus_pelanggan(id):
    db.collection("pelanggan").document(id).delete()
    return redirect('/pelanggan')


# =========================
# BOOKING
# =========================

@app.route('/booking')
def booking():
    if 'admin' not in session:
        return redirect('/login')

    keyword = request.args.get('keyword', '')
    docs = db.collection("booking").stream()
    data = []

    for doc in docs:
        item = doc.to_dict()
        item['id'] = doc.id
        
        if keyword:
            text = f"{item.get('nama_pelanggan','')} {item.get('motor','')} {item.get('keluhan','')} {item.get('mekanik','')} {item.get('status','')}".lower()
            if keyword.lower() not in text:
                continue
                
        data.append(item)

    return render_template('booking.html', data=data, keyword=keyword)


@app.route('/tambah_booking', methods=['GET', 'POST'])
def tambah_booking():
    if request.method == 'POST':
        db.collection("booking").add({
            "nama_pelanggan": request.form['nama_pelanggan'],
            "motor": request.form['motor'],
            "keluhan": request.form['keluhan'],
            "mekanik": request.form['mekanik'],
            "status": request.form['status']
        })
        return redirect('/booking')
    return render_template('tambah_booking.html')


@app.route('/edit_booking/<id>', methods=['GET', 'POST'])
def edit_booking(id):
    doc_ref = db.collection("booking").document(id)
    
    if request.method == 'POST':
        doc_ref.update({
            "nama_pelanggan": request.form['nama_pelanggan'],
            "motor": request.form['motor'],
            "keluhan": request.form['keluhan'],
            "mekanik": request.form['mekanik'],
            "status": request.form['status']
        })
        return redirect('/booking')

    data = doc_ref.get().to_dict()
    data['id'] = id
    return render_template('edit_booking.html', data=data)


@app.route('/hapus_booking/<id>')
def hapus_booking(id):
    db.collection("booking").document(id).delete()
    return redirect('/booking')


# =========================
# SPAREPART
# =========================

@app.route('/sparepart')
def sparepart():
    if 'admin' not in session:
        return redirect('/login')

    keyword = request.args.get('keyword', '')
    kategori = request.args.get('kategori', '')
    docs = db.collection("sparepart").stream()
    data = []

    for doc in docs:
        item = doc.to_dict()
        nama = item.get("nama_sparepart", "").lower()

        if "oli" in nama or "yamalube" in nama or "mpx" in nama:
            jenis = "Oli"
        elif "busi" in nama:
            jenis = "Busi"
        elif "kampas rem" in nama:
            jenis = "Kampas Rem"
        elif "kampas" in nama:
            jenis = "Kampas Kopling"
        elif "filter" in nama:
            jenis = "Filter"
        elif "aki" in nama:
            jenis = "Aki"
        elif "ban" in nama:
            jenis = "Ban"
        else:
            jenis = "Lainnya"

        if keyword and keyword.lower() not in nama:
            continue
        if kategori and kategori != jenis:
            continue

        data.append({
            "id": doc.id,
            "nama_sparepart": item.get("nama_sparepart", ""),
            "kategori": jenis,
            "stok": item.get("stok", 0),
            "harga": item.get("harga", 0)
        })

    return render_template('sparepart.html', data=data, keyword=keyword, kategori=kategori)


@app.route('/tambah_sparepart', methods=['GET', 'POST'])
def tambah_sparepart():
    if request.method == 'POST':
        db.collection("sparepart").add({
            "nama_sparepart": request.form['nama_sparepart'],
            "stok": request.form['stok'],
            "harga": request.form['harga']
        })
        return redirect('/sparepart')
    return render_template('tambah_sparepart.html')


@app.route('/edit_sparepart/<id>', methods=['GET', 'POST'])
def edit_sparepart(id):
    doc_ref = db.collection("sparepart").document(id)
    
    if request.method == 'POST':
        doc_ref.update({
            "nama_sparepart": request.form['nama_sparepart'],
            "stok": request.form['stok'],
            "harga": request.form['harga']
        })
        return redirect('/sparepart')

    data = doc_ref.get().to_dict()
    data['id'] = id
    return render_template('edit_sparepart.html', data=data)


@app.route('/hapus_sparepart/<id>')
def hapus_sparepart(id):
    db.collection("sparepart").document(id).delete()
    return redirect('/sparepart')


# =========================
# ADMIN & CUSTOMER SERVICE
# =========================

@app.route('/admin')
def admin():
    if 'admin' not in session:
        return redirect('/login')

    docs = db.collection("admins").stream()
    data = [{"id": doc.id, **doc.to_dict()} for doc in docs]

    return render_template('admin.html', data=data)


@app.route('/detail_booking/<id>')
def detail_booking(id):
    # Mengambil sparepart yang terkait dengan ID booking tertentu
    docs = db.collection("detail_booking").where("booking_id", "==", id).stream()
    sparepart = [{"id": doc.id, **doc.to_dict()} for doc in docs]
    
    # Menjumlahkan total harga (asumsi ada field 'harga' atau 'total' di dokumen)
    total = sum(float(x.get('harga', 0)) for x in sparepart)

    return render_template('detail_booking.html', sparepart=sparepart, total=total)


@app.route('/customer_service')
def customer_service():
    if 'admin' not in session:
        return redirect('/login')

    docs = db.collection("customer_service").stream()
    data = [{"id": doc.id, **doc.to_dict()} for doc in docs]

    return render_template('customer_service.html', data=data)


@app.route('/tambah_customer_service', methods=['GET', 'POST'])
def tambah_customer_service():
    if request.method == 'POST':
        db.collection("customer_service").add({
            "nama_pelanggan": request.form['nama_pelanggan'],
            "telepon": request.form['telepon'],
            "keluhan": request.form['keluhan'],
            "status": request.form['status']
        })
        return redirect('/customer_service')
    return render_template('tambah_customer_service.html')


@app.route('/hapus_customer_service/<id>')
def hapus_customer_service(id):
    db.collection("customer_service").document(id).delete()
    return redirect('/customer_service')


# =========================
# LOGOUT & RUN
# =========================

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)