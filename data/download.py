# pip install wget
import wget
 
url = "https://storage.googleapis.com/kaggle-competitions-data/kaggle-v2/52279/5822112/bundle/archive.zip?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1689506179&Signature=rI9GQacd7%2FK%2FOyrV%2BQmttcbAJWr92nknYI%2BRnVDuAYaMGPM7FAUOGWudYbETT2CDxFM2chDQ4%2BCvT%2F6B1JR5ts%2FLskDeBFrjjhiQWXsZaHKpI7nVwQRjtmp9jOKO%2B2qjSh5nAwe19rxYWb2pH%2BytBYlklrbOz8E0e5dl5fFImyGaHtnMYCDUwbRAuTlJBdyQHsQA8DFb7ErPPo96e3u2%2FZh%2BPZr1AFsMQvLyyaKtD%2BcPBIpnTRrIbzjblKG8nSrXE6VZmMDY4jBV5qlIxYt%2BePUUvyb0qdhHTQxzv9uvEH9ZA9lIoJHkw8x1yBm9rIFVnl4aaGX1zPYYYtyeyNy2yA%3D%3D&response-content-disposition=attachment%3B+filename%3Dhubmap-hacking-the-human-vasculature.zip"
output_filename = 'data.zip'  # filename
# download to current directory
wget.download(url, out=output_filename)