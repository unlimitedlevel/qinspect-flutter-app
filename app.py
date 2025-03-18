import gradio as gr

def launch_app():
    return """
    <html>
    <head>
        <meta charset="UTF-8">
        <meta content="IE=Edge" http-equiv="X-UA-Compatible">
        <meta name="description" content="QInspect - Aplikasi Manajemen Dokumen Kualitas dengan OCR">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        
        <!-- iOS meta tags & icons -->
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="black">
        <meta name="apple-mobile-web-app-title" content="QInspect">
        
        <title>QInspect App</title>
        
        <style>
        body {
            margin: 0;
            padding: 0;
            overflow: hidden;
            height: 100vh;
            width: 100vw;
        }
        
        iframe {
            border: none;
            width: 100%;
            height: 100%;
        }
        
        .loading {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
            width: 100%;
            position: absolute;
            background-color: white;
            flex-direction: column;
        }
        
        .spinner {
            border: 8px solid rgba(0, 0, 0, 0.1);
            border-radius: 50%;
            border-top: 8px solid #3498db;
            width: 60px;
            height: 60px;
            animation: spin 2s linear infinite;
            margin-bottom: 20px;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        </style>
    </head>
    <body>
        <div class="loading" id="loading">
            <div class="spinner"></div>
            <h2>Memuat Aplikasi QInspect...</h2>
            <p>Mohon tunggu sebentar</p>
        </div>
        
        <iframe 
            src="https://unlimitedlevel.github.io/qinspect-flutter-app" 
            id="app-frame"
            onload="document.getElementById('loading').style.display='none';"
        ></iframe>
    </body>
    </html>
    """

demo = gr.HTML(launch_app)

if __name__ == "__main__":
    demo.launch()