# QInspect - Aplikasi Manajemen Dokumen Kualitas dengan OCR

[![Generic badge](https://img.shields.io/badge/Flutter-Web-blue.svg)](https://flutter.dev/)
[![Generic badge](https://img.shields.io/badge/Hugging_Face-API-yellow.svg)](https://huggingface.co/)
[![Generic badge](https://img.shields.io/badge/Supabase-Database-green.svg)](https://supabase.io/)

QInspect adalah aplikasi berbasis web untuk manajemen dokumen kualitas konstruksi yang mengintegrasikan teknologi OCR dari Hugging Face. Aplikasi ini memungkinkan tim quality control untuk mengelola dokumen kualitas dengan lebih efisien.

![QInspect Screenshot](https://raw.githubusercontent.com/unlimitedlevel/qinspect-flutter-app/main/screenshots/dashboard.png)

## Cara Menggunakan

1. Navigasi ke tab "Dokumen" di bagian bawah
2. Pilih tab "Upload" untuk mengunggah dokumen baru
3. Pilih dokumen dari komputer Anda
4. Tunggu proses OCR selesai
5. Tinjau dan edit data yang diekstrak jika diperlukan
6. Klik "Simpan Dokumen" untuk menyimpan ke database

## Model AI yang Digunakan

- **OCR**: Microsoft TrOCR untuk pengenalan teks dari gambar dokumen
- **NLP**: Mistral-7B-Instruct untuk ekstraksi informasi terstruktur

## Teknologi

Aplikasi ini dibuat menggunakan:

- **Frontend**: Flutter Web
- **Backend**: Supabase (Auth, Database, Storage)
- **AI**: Hugging Face API

## Tentang Proyek

QInspect dikembangkan untuk membantu tim quality control mengelola dokumen proyek konstruksi dengan lebih efisien menggunakan teknologi AI.