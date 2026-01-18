import customtkinter as ctk
import threading
import speedtest
import time
import math
from PIL import Image
import tkinter.messagebox as messagebox

class SpeedTestApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Pencere Ayarları
        self.title("Aura SpeedTest Pro")
        self.geometry("450x620")
        self.resizable(False, False)
        
        # Tema Ayarları
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Fontlar (Daha modern bir hiyerarşi)
        self.title_font = ("Outfit", 30, "bold")
        self.metric_font = ("Outfit", 42, "bold")
        self.label_font = ("Outfit", 14, "bold")
        self.small_font = ("Outfit", 11)
        self.button_font = ("Outfit", 16, "bold")

        # Renk Paleti (Modern & Premium)
        self.bg_color = "#0f172a"  # Slate 900
        self.card_bg = "#1e293b"   # Slate 800
        self.accent_blue = "#38bdf8" # Sky 400
        self.accent_green = "#34d399" # Emerald 400
        self.text_dim = "#94a3b8"   # Slate 400

        # Animasyon Değişkenleri
        self.animating = False
        self.pulse_val = 0
        
        self.setup_ui()

    def setup_ui(self):
        self.configure(fg_color=self.bg_color)
        
        # Header (Minimalist & Şık)
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.pack(pady=(40, 20), padx=40, fill="x")

        self.title_label = ctk.CTkLabel(
            self.header_frame, 
            text="AURA SPEEDTEST", 
            font=self.title_font,
            text_color=self.accent_blue
        )
        self.title_label.pack(side="left")

        # Ana İçerik Alanı
        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.pack(pady=10, padx=40, fill="both", expand=True)

        # Ping Kartı (Üstte Küçük ve Zarif)
        self.ping_card = ctk.CTkFrame(self.main_container, corner_radius=15, fg_color=self.card_bg, height=50)
        self.ping_card.pack(pady=(0, 20), fill="x")
        self.ping_card.pack_propagate(False)
        
        self.ping_label = ctk.CTkLabel(self.ping_card, text="PING: -- ms", font=self.label_font, text_color=self.text_dim)
        self.ping_label.pack(expand=True)

        # Download & Upload Kartları (Yan Yana değil, daha etkileyici dikey dizilim)
        self.down_card = self.create_metric_card(self.main_container, "İNDİRME", "0.0", self.accent_blue, "⏬")
        self.up_card = self.create_metric_card(self.main_container, "YÜKLEME", "0.0", self.accent_green, "⏫")

        # Footer (Buton ve Progress)
        self.footer_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.footer_frame.pack(pady=(20, 40), padx=40, fill="x")

        self.progress_bar = ctk.CTkProgressBar(
            self.footer_frame, 
            mode="indeterminate", 
            height=6, 
            progress_color=self.accent_blue,
            fg_color="#334155"
        )
        self.progress_bar.set(0)
        
        self.start_button = ctk.CTkButton(
            self.footer_frame, 
            text="TESTİ BAŞLAT", 
            height=60, 
            font=self.button_font,
            corner_radius=18,
            fg_color=self.accent_blue,
            hover_color="#0ea5e9",
            text_color="#0f172a",
            command=self.start_test_sequence
        )
        self.start_button.pack(fill="x")

    def create_metric_card(self, parent, title, value, color, icon):
        card = ctk.CTkFrame(parent, corner_radius=25, fg_color=self.card_bg, border_width=1, border_color="#334155")
        card.pack(pady=10, fill="x")
        
        # İç Padding için Frame
        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(pady=20, padx=25, fill="x")

        title_label = ctk.CTkLabel(inner, text=f"{icon} {title}", font=self.label_font, text_color=color)
        title_label.pack(anchor="w")

        val_label = ctk.CTkLabel(inner, text=value, font=self.metric_font, text_color="#f8fafc")
        val_label.pack(anchor="w", pady=(5, 0))
        
        unit_label = ctk.CTkLabel(inner, text="Mbps", font=self.small_font, text_color=self.text_dim)
        unit_label.pack(anchor="w")

        # Değere programatik erişim için karta label'ı ekle
        if "İNDİRME" in title: self.down_val = val_label
        else: self.up_val = val_label
        
        return card

    def toggle_theme(self):
        mode = "dark" if self.theme_switch.get() == "dark" else "light"
        ctk.set_appearance_mode(mode)

    def animate_counter(self, label, target_val, current_val=0):
        if current_val < target_val:
            step = (target_val - current_val) / 5
            if step < 0.1: step = 0.1
            new_val = min(current_val + step, target_val)
            label.configure(text=f"{new_val:.1f}")
            self.after(20, lambda: self.animate_counter(label, target_val, new_val))

    def pulse_animation(self):
        if not self.animating:
            self.down_card.configure(border_color=["#e2e8f0", "#334155"])
            self.up_card.configure(border_color=["#e2e8f0", "#334155"])
            return

        # Sinüs dalgası ile parlama efekti
        self.pulse_val += 0.1
        alpha = (math.sin(self.pulse_val) + 1) / 2
        
        # Mavi ve yeşil arası parlama
        color = "#3b82f6" if int(self.pulse_val) % 2 == 0 else "#10b981"
        self.down_card.configure(border_color=color)
        self.up_card.configure(border_color=color)
        
        self.after(50, self.pulse_animation)

    def start_test_sequence(self):
        self.animating = True
        self.start_button.configure(state="disabled", text="Ölçülüyor...")
        self.progress_bar.pack(fill="x", pady=(0, 10))
        self.progress_bar.start()
        
        # Reset labels with fade-out feel
        self.down_val.configure(text="0.0")
        self.up_val.configure(text="0.0")
        self.ping_label.configure(text="PING: -- ms")

        
        self.pulse_animation()
        
        thread = threading.Thread(target=self.perform_speed_test, daemon=True)
        thread.start()

    def perform_speed_test(self):
        try:
            st = speedtest.Speedtest()
            st.get_best_server()
            
            # Ping
            ping = round(st.results.ping)
            self.after(0, lambda: self.ping_label.configure(text=f"PING: {ping} ms"))


            # Download
            d_speed = st.download() / 1_000_000
            self.after(0, lambda: self.animate_counter(self.down_val, d_speed))

            # Upload
            u_speed = st.upload() / 1_000_000
            self.after(0, lambda: self.animate_counter(self.up_val, u_speed))

        except Exception as e:
            error_msg = str(e)
            self.after(0, lambda msg=error_msg: messagebox.showerror("Hata", f"Test başarısız oldu:\n{msg}"))
        
        finally:
            self.after(1000, self.finalize_test)

    def finalize_test(self):
        self.animating = False
        self.progress_bar.stop()
        self.progress_bar.pack_forget()
        self.start_button.configure(state="normal", text="Yeniden Test Et")

if __name__ == "__main__":
    app = SpeedTestApp()
    app.mainloop()
