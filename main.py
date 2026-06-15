import os
import urllib.parse
import subprocess
import sys
import flet as ft

IMAGE_FIT_CONTAIN = "contain"
IMAGE_FIT_COVER = "cover"
PROFILE_NAME = "Pombili Hamwoomo"
PROFILE_ROLE = "Mining Student"
PROFILE_EMAIL = "pombilihamwoomo@gmail.com"
PROFILE_IMAGE = "Profile pic.jpeg"
PROFILE_GITHUB = "https://github.com/pombilihamwoomo-dot/MiningChecklistApp.git"
PROFILE_LINKEDIN = "https://www.linkedin.com/"

BG = "#0b0f12"
PANEL = "#141b22"
PANEL_2 = "#1b252f"
INK = "#f4f7f8"
STEEL = "#c8d1d8"
MUTED = "#91a0aa"
COPPER = "#d08345"
GOLD = "#f2b84b"
GREEN = "#7ea66a"
CYAN = "#67c7d8"
LINE = "#313c45"


def main(page: ft.Page):
    page.title = f"{PROFILE_NAME} Portfolio"
    page.theme_mode = ft.ThemeMode.DARK
    page.theme = ft.Theme(color_scheme_seed=COPPER, font_family="Times New Roman")
    page.bgcolor = BG
    page.padding = 0
    page.spacing = 0
    page.scroll = ft.ScrollMode.AUTO
    page.window_min_width = 1000
    page.window_min_height = 720

    active_key = "home"

    ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))

    def snack(message: str):
        page.snack_bar = ft.SnackBar(ft.Text(message), open=True)
        page.update()

    def card(content, width=None):
        return ft.Container(
            content=content,
            width=width,
            padding=26,
            border_radius=8,
            bgcolor=PANEL,
            border=ft.Border(
                left=ft.BorderSide(1, LINE),
                top=ft.BorderSide(1, LINE),
                right=ft.BorderSide(1, LINE),
                bottom=ft.BorderSide(1, LINE),
            ),
        )

    def heading(title: str, subtitle: str):
        return ft.Column(
            [
                ft.Text(title, size=44, weight=ft.FontWeight.W_800, color=INK, text_align=ft.TextAlign.CENTER),
                ft.Container(width=110, height=5, bgcolor=COPPER, border_radius=2),
                ft.Text(subtitle, size=20, color=MUTED, text_align=ft.TextAlign.CENTER),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        )

    def shell(content):
        return ft.Container(
            expand=True,
            padding=ft.Padding(40, 42, 40, 42),
            content=ft.Column(
                [content],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=0,
            ),
        )

    def open_project(name: str):
        snack(f"{name} page opened.")

    def open_certificate(filename: str):
        if page.web:
            page.launch_url(f"/{filename}")
            return
        pdf_path = os.path.join(ASSETS_DIR, filename)
        try:
            if sys.platform == "win32":
                os.startfile(pdf_path)
            elif sys.platform == "darwin":
                subprocess.Popen(["open", pdf_path])
            else:
                subprocess.Popen(["xdg-open", pdf_path])
        except Exception as e:
            snack(f"Could not open PDF: {e}")

    def open_video(filename: str):
        if page.web:
            page.launch_url(f"/{filename}")
            return
        video_path = os.path.join(ASSETS_DIR, filename)
        try:
            if sys.platform == "win32":
                os.startfile(video_path)
            elif sys.platform == "darwin":
                subprocess.Popen(["open", video_path])
            else:
                subprocess.Popen(["xdg-open", video_path])
        except Exception as e:
            snack(f"Could not open video: {e}")

    def get_certificates_from_assets(assets_dir):
        certs = []
        if not os.path.exists(assets_dir):
            return certs
        for filename in os.listdir(assets_dir):
            if filename.lower().endswith(".pdf") and os.path.isfile(os.path.join(assets_dir, filename)):
                title = os.path.splitext(filename)[0].replace("_", " ")
                description = f"Proof of completion for {title}."
                certs.append((title, description, filename))
        return certs

    def contact_submit(_):
        if not name_field.value or not email_field.value or not message_field.value:
            snack("Please fill in your name, email, and message.")
            return
        snack(f"Thanks, {name_field.value}! Your message is ready.")
        name_field.value = ""
        email_field.value = ""
        message_field.value = ""
        page.update()

    skills = [
        ("Python", "Data processing, automation, and small engineering apps.", ft.Icons.TERMINAL, CYAN),
        ("Flet", "Interactive web interfaces built with Python.", ft.Icons.WEB_ASSET, COPPER),
        ("MATLAB", "Engineering calculations, plots, and simulations.", ft.Icons.AUTO_GRAPH, GOLD),
        ("HTML/CSS", "Responsive layouts and visual presentation.", ft.Icons.DESIGN_SERVICES, GREEN),
        ("Mining Engineering", "Resource extraction, mine safety, and sustainability.", ft.Icons.CONSTRUCTION, COPPER),
        ("GitHub", "Version control and project publishing.", ft.Icons.CODE, CYAN),
    ]

    projects = [
        ("Mine Ventilation Sim", "Simulate and visualize airflow and gas concentrations in underground mines.", ft.Icons.AIR, COPPER),
        ("Ore Production Tracker", "Plot extraction rates and analyze machinery downtime and efficiency.", ft.Icons.SHOW_CHART, CYAN),
        ("Field Exploration Log", "Record geological samples, ore grades, and site observations.", ft.Icons.FACT_CHECK, GREEN),
    ]

    certificates = get_certificates_from_assets(ASSETS_DIR)

    timeline = [
        ("Week 1", "Planned the portfolio structure and identified mining engineering concepts to cover: extraction methods, safety protocols, and resource management.", "Completed"),
        ("Week 2", "Completed MATLAB Onramp and Simulink Onramp certificates. Used MATLAB to verify geological models featured in the blog posts.", "Completed"),
        ("Week 3", "Wrote project reflection with real-world mining examples, including Namibian mining context and safety standards.", "Completed"),
        ("Week 4", "Completed various MathWorks certificates covering Machine Learning, matrix operations, vector calculations, and MATLAB Desktop Tools.", "Completed"),
        ("Week 5", "Built and tested the full Flet portfolio app — home, skills, projects, MATLAB hub, GitHub, school, timeline, blog, and contact pages.", "Completed"),
        ("Week 6", "Reviewed all content for technical accuracy, fixed the PDF certificate launcher, linked video resources, and prepared the portfolio for final submission.", "Completed"),
    ]

    home_page = ft.Container(
        expand=True,
        padding=ft.Padding(40, 42, 40, 42),
        content=ft.Column(
            [
                heading("About Me", "Engineering curiosity with a programmer's toolkit."),
                ft.Container(height=24),
                card(
                    ft.Column(
                        [
                            ft.CircleAvatar(
                                foreground_image_src=PROFILE_IMAGE,
                                radius=110,
                                bgcolor=PANEL_2,
                            ),
                            ft.Text(PROFILE_NAME, size=26, color=INK, weight=ft.FontWeight.W_800),
                            ft.Text("Mining Student 225067250", size=17, color=MUTED),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=14,
                    ),
                    width=500,
                ),
                ft.Container(height=24),
                card(
                    ft.Column(
                        [
                            ft.Text(
                                "I am a mining engineering student interested in computer programming because both"
                                " fields reward clear thinking. In mining engineering, I study resource extraction, safety,"
                                " and sustainability. In programming, I turn those ideas into useful tools and visual interfaces.",
                                size=22,
                                color=STEEL,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Text(
                                "This portfolio is designed to show both sides: mining engineering knowledge"
                                " and practical software skill.",
                                size=18,
                                color=MUTED,
                                text_align=ft.TextAlign.CENTER,
                            ),
                        ],
                        spacing=14,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    width=900,
                ),
                ft.Container(height=24),
                ft.Row(
                    [
                        ft.FilledButton("Open Projects", icon=ft.Icons.WORK, on_click=lambda _: show_page("projects")),
                        ft.OutlinedButton("Contact", icon=ft.Icons.EMAIL, on_click=lambda _: show_page("contact")),
                    ],
                    spacing=16,
                    alignment=ft.MainAxisAlignment.CENTER,
                    wrap=True,
                ),
                ft.Container(height=40),
                ft.Row(
                    [
                        card(ft.Column([ft.Text("Extraction", size=34, weight=ft.FontWeight.W_800), ft.Text("Mining Logic", size=17, color=MUTED)], spacing=5), width=230),
                        card(ft.Column([ft.Text("Python", size=34, weight=ft.FontWeight.W_800), ft.Text("Code experiments", size=17, color=MUTED)], spacing=5), width=250),
                        card(ft.Column([ft.Text("Lab + UI", size=34, weight=ft.FontWeight.W_800), ft.Text("Useful tools", size=17, color=MUTED)], spacing=5), width=250),
                    ],
                    spacing=12,
                    wrap=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    skills_page = shell(
        ft.Column(
            [
                heading("Skills", "Tools for turning engineering ideas into working software."),
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            col={"sm": 12, "md": 6, "lg": 4},
                            content=card(
                                ft.Column(
                                    [
                                        ft.Icon(icon, color=color, size=48),
                                        ft.Text(title, size=25, weight=ft.FontWeight.W_800, color=INK),
                                        ft.Text(desc, size=17, color=MUTED),
                                    ],
                                    spacing=10,
                                )
                            ),
                        )
                        for title, desc, icon, color in skills
                    ],
                    spacing=14,
                    run_spacing=14,
                ),
            ],
            spacing=22,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    projects_page = shell(
        ft.Column(
            [
                heading("Projects", "Portfolio ideas shaped around mining engineering, data, and UI."),
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            content=card(
                                ft.Column(
                                    [
                                        ft.Icon(icon, color=color, size=54),
                                        ft.Text(title, size=25, weight=ft.FontWeight.W_800, color=INK),
                                        ft.Text(desc, size=17, color=MUTED),
                                        ft.OutlinedButton(
                                            "View Concept",
                                            icon=ft.Icons.OPEN_IN_FULL,
                                            on_click=lambda _, project=title: open_project(project),
                                        ),
                                    ],
                                    spacing=12,
                                )
                            ),
                        )
                        for title, desc, icon, color in projects
                    ],
                    spacing=14,
                    run_spacing=14,
                ),
            ],
            spacing=22,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    matlab_page = shell(
        ft.Column(
            [
                heading("MATLAB Certificates", "Technical milestones that support engineering computation."),
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            content=card(
                                ft.Column(
                                    [
                                        ft.Icon(ft.Icons.MILITARY_TECH, color=GOLD, size=52),
                                        ft.Text(title, size=24, weight=ft.FontWeight.W_800, color=INK),
                                        ft.Text(desc, size=17, color=MUTED),
                                        ft.FilledButton(
                                            "Open PDF",
                                            icon=ft.Icons.OPEN_IN_NEW,
                                            on_click=lambda _, fn=file_name: open_certificate(fn),
                                        ),
                                    ],
                                    spacing=12,
                                )
                            ),
                        )
                        for title, desc, file_name in certificates
                    ],
                    spacing=14,
                    run_spacing=14,
                ),
            ],
            spacing=22,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    github_page = shell(
        ft.Column(
            [
                heading("GitHub Evidence", "Individual contribution record — commits, pull requests, and impact."),
                ft.Container(height=8),
                card(
                    ft.Row(
                        [
                            ft.Container(
                                width=80, height=80, border_radius=40,
                                bgcolor=PANEL_2,
                                alignment=ft.Alignment(0, 0),
                                content=ft.Icon(ft.Icons.PERSON, color=CYAN, size=48),
                            ),
                            ft.Column(
                                [
                                    ft.Text("pombili-hamwoomo", size=26, weight=ft.FontWeight.W_800, color=INK),
                                    ft.Text("Pombili Hamwoomo · Mining Engineering Student", size=16, color=MUTED),
                                    ft.Text("University of Namibia · Jose Eduardo Campus", size=15, color=MUTED),
                                    ft.FilledButton(
                                        "View GitHub Profile",
                                        icon=ft.Icons.OPEN_IN_NEW,
                                        url=PROFILE_GITHUB,
                                    ),
                                ],
                                spacing=6,
                                expand=True,
                            ),
                        ],
                        spacing=20,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    width=1000,
                ),
                ft.Container(height=14),
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            content=card(ft.Column([
                                ft.Icon(ft.Icons.COMMIT, color=COPPER, size=40),
                                ft.Text("Commit History", size=20, weight=ft.FontWeight.W_800, color=INK),
                                ft.Text(
                                    "Regular commits were made throughout the 6-week project, "
                                    "covering portfolio structure, blog content, MATLAB integration, "
                                    "and bug fixes including the PDF launcher.",
                                    size=15, color=STEEL,
                                ),
                            ], spacing=10)),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            content=card(ft.Column([
                                ft.Icon(ft.Icons.MERGE_TYPE, color=CYAN, size=40),
                                ft.Text("Pull Requests", size=20, weight=ft.FontWeight.W_800, color=INK),
                                ft.Text(
                                    "Pull requests were submitted for each major feature: "
                                    "the blog page, MATLAB certificate hub, timeline updates, "
                                    "and the GitHub evidence section.",
                                    size=15, color=STEEL,
                                ),
                            ], spacing=10)),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            content=card(ft.Column([
                                ft.Icon(ft.Icons.SUMMARIZE, color=GREEN, size=40),
                                ft.Text("Impact Summary", size=20, weight=ft.FontWeight.W_800, color=INK),
                                ft.Text(
                                    "Contributed the individual portfolio module covering mining "
                                    "engineering concepts, MATLAB certificates, and the technical blog "
                                    "with worked examples relevant to the engineering curriculum.",
                                    size=15, color=STEEL,
                                ),
                            ], spacing=10)),
                        ),
                    ],
                    spacing=14, run_spacing=14,
                ),
                ft.Container(height=14),
                card(
                    ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Icon(ft.Icons.PHOTO_LIBRARY, color=GOLD, size=28),
                                    ft.Text("Commit Screenshot", size=20, weight=ft.FontWeight.W_800, color=INK),
                                ],
                                spacing=10,
                            ),
                            ft.Container(
                                height=260,
                                border_radius=8,
                                bgcolor=PANEL_2,
                                alignment=ft.Alignment(0, 0),
                                content=ft.Image(
                                    src="commits.png",
                                    fit=IMAGE_FIT_CONTAIN,
                                    width=900,
                                    height=250,
                                ),
                            ),
                            ft.Text(
                                "Screenshot of commit history from the group repository on GitHub.",
                                size=14, color=MUTED, text_align=ft.TextAlign.CENTER,
                            ),
                        ],
                        spacing=12,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    width=1000,
                ),
            ],
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    school_page = shell(
        ft.Column(
            [
                heading("School", "Where knowledge and engineering come together."),
                card(
                    ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Container(
                                        width=100,
                                        height=100,
                                        border_radius=12,
                                        bgcolor=ft.Colors.WHITE,
                                        alignment=ft.Alignment(0, 0),
                                        content=ft.Image(
                                            src="unam logo.jpeg",
                                            width=90,
                                            height=90,
                                            fit=IMAGE_FIT_CONTAIN,
                                        ),
                                    ),
                                    ft.Column(
                                        [
                                            ft.Text("University of Namibia", size=32, weight=ft.FontWeight.W_800, color=INK),
                                            ft.Text("Jose Eduardo Engineering Campus", size=20, color=COPPER, weight=ft.FontWeight.W_600),
                                            ft.Text("Bachelor of Engineering — Mining", size=17, color=MUTED),
                                        ],
                                        spacing=6,
                                        expand=True,
                                    ),
                                ],
                                spacing=24,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            ft.Container(height=1, bgcolor=LINE),
                            ft.Row(
                                [
                                    ft.Container(
                                        expand=True,
                                        padding=16,
                                        border_radius=8,
                                        bgcolor=ft.Colors.with_opacity(0.10, COPPER),
                                        content=ft.Column(
                                            [
                                                ft.Icon(ft.Icons.LOCATION_ON, color=COPPER, size=28),
                                                ft.Text("Location", size=15, color=MUTED),
                                                ft.Text("Ongwediva Constituency,\nOshana Region", size=18, color=INK, weight=ft.FontWeight.W_700, text_align=ft.TextAlign.CENTER),
                                            ],
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            spacing=6,
                                        ),
                                    ),
                                    ft.Container(
                                        expand=True,
                                        padding=16,
                                        border_radius=8,
                                        bgcolor=ft.Colors.with_opacity(0.10, CYAN),
                                        content=ft.Column(
                                            [
                                                ft.Icon(ft.Icons.SCIENCE, color=CYAN, size=28),
                                                ft.Text("Faculty", size=15, color=MUTED),
                                                ft.Text("Faculty of Engineering", size=18, color=INK, weight=ft.FontWeight.W_700, text_align=ft.TextAlign.CENTER),
                                            ],
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            spacing=6,
                                        ),
                                    ),
                                    ft.Container(
                                        expand=True,
                                        padding=16,
                                        border_radius=8,
                                        bgcolor=ft.Colors.with_opacity(0.10, GREEN),
                                        content=ft.Column(
                                            [
                                                ft.Icon(ft.Icons.VERIFIED, color=GREEN, size=28),
                                                ft.Text("Status", size=15, color=MUTED),
                                                ft.Text("Currently Enrolled", size=18, color=INK, weight=ft.FontWeight.W_700, text_align=ft.TextAlign.CENTER),
                                            ],
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            spacing=6,
                                        ),
                                    ),
                                ],
                                spacing=14,
                            ),
                        ],
                        spacing=20,
                    ),
                    width=1000,
                ),
            ],
            spacing=22,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    timeline_page = shell(
        ft.Column(
            [
                heading("Timeline", "How the portfolio grows from learning to technical tools."),
                card(
                    ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Container(
                                        width=86,
                                        padding=ft.Padding(0, 12, 0, 12),
                                        bgcolor=ft.Colors.with_opacity(0.14, COPPER),
                                        border_radius=8,
                                        alignment=ft.Alignment(0, 0),
                                        content=ft.Text(week, size=19, color=COPPER, weight=ft.FontWeight.W_800),
                                    ),
                                    ft.Column(
                                        [
                                            ft.Text(subtitle, size=19, color=STEEL, weight=ft.FontWeight.W_600),
                                            ft.Text("Progress: " + status, size=14, color=GOLD),
                                        ],
                                        spacing=6,
                                        expand=True,
                                    ),
                                ],
                                spacing=14,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            )
                            for week, subtitle, status in timeline
                        ],
                        spacing=12,
                    ),
                    width=1120,
                ),
            ],
            spacing=22,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    name_field = ft.TextField(label="Your Name", text_size=18, border_radius=8)
    email_field = ft.TextField(label="Your Email", text_size=18, border_radius=8)
    message_field = ft.TextField(
        label="Your Message", text_size=18, multiline=True, min_lines=6, max_lines=8, border_radius=8
    )

    contact_page = shell(
        ft.Column(
            [
                heading("Contact", "Send a quick note about code, mining engineering, or collaboration."),
                card(
                    ft.Column(
                        [
                            name_field,
                            email_field,
                            message_field,
                            ft.Row(
                                [
                                    ft.FilledButton("Send Message", icon=ft.Icons.SEND, on_click=contact_submit),
                                    ft.OutlinedButton(
                                        "Back Home",
                                        icon=ft.Icons.HOME,
                                        on_click=lambda _: show_page("home"),
                                    ),
                                ],
                                spacing=12,
                                wrap=True,
                            ),
                        ],
                        spacing=14,
                    ),
                    width=980,
                ),
            ],
            spacing=22,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    blog_page = shell(
        ft.Column(
            [
                heading("Technical Blog", "Project Reflection"),
                card(
                    ft.Column(
                        [
                            ft.Text("225067250 Pombili Reflection", size=24, weight=ft.FontWeight.W_800, color=INK),
                            ft.Container(height=10),
                            ft.Container(
                                height=260,
                                border_radius=8,
                                bgcolor=PANEL_2,
                                alignment=ft.Alignment(0, 0),
                                content=ft.Column(
                                    [
                                        ft.Icon(ft.Icons.PLAY_CIRCLE_FILLED, color=COPPER, size=64),
                                        ft.FilledButton(
                                            "Watch Reflection Video on GitHub",
                                            icon=ft.Icons.OPEN_IN_NEW,
                                            url="https://github.com/pombilihamwoomo-dot/MiningChecklistApp/blob/main/225067250_pombili_reflection.mp4.mp4",
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=15,
                                ),
                            ),
                            ft.Container(height=10),
                            ft.Text(
                                "A detailed reflection on the development of the Mining Engineering toolkit "
                                "and portfolio application.",
                                size=16, color=MUTED, text_align=ft.TextAlign.CENTER,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10,
                    ),
                    width=1000,
                ),
            ],
            spacing=26,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    pages = {
        "home": home_page,
        "skills": skills_page,
        "projects": projects_page,
        "matlab": matlab_page,
        "github": github_page,
        "school": school_page,
        "timeline": timeline_page,
        "blog": blog_page,
        "contact": contact_page,
    }

    page_host = ft.Column([], expand=True, alignment=ft.MainAxisAlignment.CENTER)
    nav_buttons = {}

    def nav_style(is_active: bool):
        return ft.ButtonStyle(
            color=INK,
            bgcolor=ft.Colors.with_opacity(0.20, COPPER) if is_active else ft.Colors.TRANSPARENT,
            shape=ft.RoundedRectangleBorder(radius=8),
            text_style=ft.TextStyle(size=17, weight=ft.FontWeight.W_700),
            padding=ft.Padding(16, 14, 16, 14),
        )

    def set_nav_styles():
        for key, button in nav_buttons.items():
            button.style = nav_style(key == active_key)

    def show_page(key: str):
        nonlocal active_key
        active_key = key
        page_host.controls.clear()
        page_host.controls.append(pages[key])
        set_nav_styles()
        page.update()

    def make_nav(label: str, key: str, icon: str):
        button = ft.TextButton(
            label,
            icon=icon,
            style=nav_style(key == active_key),
            on_click=lambda _, page_key=key: show_page(page_key),
        )
        nav_buttons[key] = button
        return button

    nav_items = [
        ("Home", "home", ft.Icons.HOME),
        ("Skills", "skills", ft.Icons.BUILD),
        ("Projects", "projects", ft.Icons.WORK),
        ("MATLAB", "matlab", ft.Icons.AUTO_GRAPH),
        ("GitHub", "github", ft.Icons.CODE),
        ("School", "school", ft.Icons.SCHOOL),
        ("Timeline", "timeline", ft.Icons.TIMELINE),
        ("Blog", "blog", ft.Icons.ARTICLE),
        ("Contact", "contact", ft.Icons.EMAIL),
    ]

    desktop_nav = ft.Row(
        [make_nav(label, key, icon) for label, key, icon in nav_items], spacing=4, wrap=True
    )
    mobile_nav = ft.PopupMenuButton(
        icon=ft.Icons.MENU,
        tooltip="Open pages",
        items=[
            ft.PopupMenuItem(
                content=ft.Row(
                    [ft.Icon(icon, size=18, color=COPPER), ft.Text(label)], spacing=10, tight=True
                ),
                on_click=lambda _, page_key=key: show_page(page_key),
            )
            for label, key, icon in nav_items
        ],
    )

    def update_nav_visibility(_=None):
        width = page.width or 1200
        desktop_nav.visible = width >= 900
        mobile_nav.visible = width < 900
        page.update()

    page.on_resize = update_nav_visibility

    page.appbar = ft.AppBar(
        title=ft.Container(
            width=48,
            height=48,
            border_radius=8,
            bgcolor=COPPER,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            alignment=ft.Alignment(0, 0),
            content=ft.Image(
                src="unam logo.jpeg",
                width=48,
                height=48,
                fit=IMAGE_FIT_COVER,
            ),
        ),
        bgcolor=BG,
        actions=[desktop_nav, mobile_nav],
    )

    page.add(
        ft.Container(
            height=8,
            gradient=ft.LinearGradient(
                colors=["#3a3a3a", "#5a5a5a", "#8a8a8a", "#d0d0d0"],
                begin=ft.Alignment(-1, 0),
                end=ft.Alignment(1, 0),
            ),
        ),
        page_host,
        ft.Container(
            padding=ft.Padding(40, 18, 40, 18),
            border=ft.Border(top=ft.BorderSide(1, LINE)),
            content=ft.Text(
                "2026 Pombili Hamwoomo | Mining student portfolio built with Flet",
                color=MUTED,
                size=16,
            ),
        ),
    )
    show_page("home")
    update_nav_visibility()


if __name__ == "__main__":
    assets_path = os.path.dirname(os.path.abspath(__file__))
    ft.run(main, view=ft.AppView.FLET_APP, assets_dir=assets_path)