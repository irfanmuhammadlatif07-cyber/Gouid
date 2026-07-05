# GoPay Insight Dashboard

Dashboard interaktif untuk menampilkan insight pengalaman pengguna GoPay berdasarkan data survei dan ulasan pengguna. Dashboard ini dibangun dalam format HTML/CSS/JavaScript (menggunakan Chart.js untuk visualisasi data) dan di-deploy sebagai web app menggunakan Streamlit.

## Isi Dashboard

- **KPI Cards** — ringkasan angka penting (jumlah responden, ulasan, skor kuesioner, sentimen, dll)
- **Grafik interaktif** — donut chart, bar chart, radar chart, dan line chart untuk berbagai indikator
- **Navigasi tab** — berpindah antar halaman/topik insight tanpa reload

## Struktur File

| File | Fungsi |
|---|---|
| `app.py` | Entry point Streamlit, membaca dan menampilkan `dashboard.html` |
| `dashboard.html` | Dashboard utama (HTML, CSS, JavaScript, Chart.js) |
| `requirements.txt` | Daftar dependensi Python yang dibutuhkan |

## Cara Menjalankan Secara Lokal

```bash
pip install -r requirements.txt
streamlit run app.py
```

Dashboard akan terbuka otomatis di browser pada `http://localhost:8501`.

## Deployment

Dashboard ini di-deploy secara publik menggunakan [Streamlit Community Cloud](https://share.streamlit.io).

## Sumber Data

Data KPI dan indikator berasal dari survei dan ulasan pengguna GoPay yang telah diolah dan dianonimkan.
