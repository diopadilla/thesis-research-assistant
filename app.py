from pyngrok import ngrok
ngrok.set_auth_token("2z32Me55fPbdo4Vg3Nn5RPt3TDR_82obFfWNgxWXrgApZe24h")

ngrok.kill()
public_url = ngrok.connect(8501)
print(f"ngrok tunnel: {public_url}")