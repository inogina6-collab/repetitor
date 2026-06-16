"""Генератор index.html для лендинга Домашка.AI."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "index.html"

html_content = """<!DOCTYPE html>
<html lang="ru" class="lightScroll">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Домашка.AI — Твой личный ИИ-репетитор</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700&family=Unbounded:wght@500;700;800;900&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        body {
            font-family: 'Onest', sans-serif;
            background-color: #FAF9F5;
            color: #121316;
            overflow-x: hidden;
            line-height: 1.65;
            -webkit-font-smoothing: antialiased;
        }
        .font-title {
            font-family: 'Unbounded', sans-serif;
            letter-spacing: -0.02em;
        }
        .hero-title {
            font-family: 'Unbounded', sans-serif;
            font-weight: 800;
            line-height: 1.35;
            letter-spacing: -0.03em;
        }
        .hero-title .line {
            display: block;
        }
        .hero-title .line + .line {
            margin-top: 0.35em;
        }
        .section-title {
            line-height: 1.4;
            letter-spacing: -0.02em;
        }
        .prose-spacing {
            line-height: 1.8;
        }
        .hero-subtitle {
            line-height: 1.75;
            letter-spacing: 0.01em;
        }
        
        /* АНИМАЦИЯ ПОЭТАПНОГО ПОЯВЛЕНИЯ ИНТЕРФЕЙСА (Premium Fade Up) */
        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(24px); filter: blur(4px); }
            to { opacity: 1; transform: translateY(0); filter: blur(0); }
        }
        .animate-fade-up {
            animation: fadeUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }
        .delay-1 { animation-delay: 0.12s; opacity: 0; }
        .delay-2 { animation-delay: 0.24s; opacity: 0; }
        .delay-3 { animation-delay: 0.36s; opacity: 0; }

        /* ИНТЕНСИВНОЕ ПОКАЧИВАНИЕ И ПОЛЕТ ДЕКОРАТИВНЫХ ФОРМУЛ И КНИГ */
        @keyframes deepFloat {
            0% { transform: translateY(0px) translateX(0px) rotate(0deg); opacity: 0.25; }
            33% { transform: translateY(-18px) translateX(10px) rotate(4deg); opacity: 0.55; }
            66% { transform: translateY(10px) translateX(-8px) rotate(-3deg); opacity: 0.4; }
            100% { transform: translateY(0px) translateX(0px) rotate(0deg); opacity: 0.25; }
        }
        .floating-math {
            animation: deepFloat 9s ease-in-out infinite;
        }
        .floating-math:nth-child(2) { animation-delay: 1.5s; animation-duration: 11s; }
        .floating-math:nth-child(3) { animation-delay: 3s; animation-duration: 8s; }
        .floating-math:nth-child(4) { animation-delay: 4.5s; animation-duration: 13s; }
        .floating-math:nth-child(5) { animation-delay: 2.5s; animation-duration: 10s; }
        .floating-math:nth-child(6) { animation-delay: 5.5s; animation-duration: 12s; }
        .floating-math:nth-child(7) { animation-delay: 0.5s; animation-duration: 7s; }
        
        /* ЭФФЕКТ СВЕРХЧЁТКОГО ЛАЗЕРНОГО ИИ-СКАНЕРА */
        @keyframes laserScan {
            0% { top: 0%; opacity: 0; }
            15% { opacity: 1; }
            85% { opacity: 1; }
            100% { top: 100%; opacity: 0; }
        }
        .scanner-line {
            position: absolute;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(90deg, transparent, #0052FF, #BE123C, #0052FF, transparent);
            box-shadow: 0 0 16px #0052FF, 0 0 32px #BE123C;
            animation: laserScan 2.2s ease-in-out infinite;
        }

        /* Кастомный видимый скроллбар */
        .lightScroll::-webkit-scrollbar { width: 10px; }
        .lightScroll::-webkit-scrollbar-track { background: #FAF9F5; }
        .lightScroll::-webkit-scrollbar-thumb { background: #CBD5E1; border-radius: 6px; border: 2px solid #FAF9F5; }
        .lightScroll::-webkit-scrollbar-thumb:hover { background: #94A3B8; }

        /* Мягкий градиентный фон hero-секции */
        #hero::before {
            content: '';
            position: absolute;
            inset: -20% 0 auto 0;
            height: 70%;
            background: radial-gradient(ellipse 80% 60% at 50% 0%, rgba(0, 82, 255, 0.06) 0%, transparent 70%);
            pointer-events: none;
            z-index: -1;
        }
    </style>
</head>
<body class="bg-[#FAF9F5] text-[#121316] min-h-screen antialiased selection:bg-[#0052FF] selection:text-white">

    <div class="absolute inset-0 pointer-events-none overflow-hidden z-0 opacity-80">
        <div class="floating-math absolute top-20 left-[6%] text-[#0052FF] font-mono text-xl font-bold">x = (-b ± √D) / 2a</div>
        <div class="floating-math absolute top-40 right-[8%] text-[#BE123C] font-mono text-2xl font-bold">2H₂ + O₂ → 2H₂O</div>
        <div class="floating-math absolute top-[28%] left-[4%] text-emerald-600 text-3xl font-black border-3 border-emerald-500/40 px-3 py-1 rounded-2xl rotate-[-12deg] bg-white shadow-sm">5+</div>
        <div class="floating-math absolute top-[55%] right-[5%] text-amber-600 text-5xl filter drop-shadow-md">📓</div>
        <div class="floating-math absolute top-[72%] left-[8%] text-indigo-600 font-mono text-lg font-bold">sin²α + cos²α = 1</div>
        <div class="floating-math absolute top-[15%] left-[45%] text-[#0052FF]/30 text-6xl filter drop-shadow-sm">📐</div>
        <div class="floating-math absolute top-[35%] right-[42%] text-purple-600 font-mono text-lg font-bold">C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O</div>
        <div class="floating-math absolute top-[65%] left-[3%] text-rose-600 font-mono text-xl font-bold">F = m · a</div>
        <div class="floating-math absolute top-[85%] right-[15%] text-cyan-600 text-5xl filter drop-shadow-md">📚</div>
        <div class="floating-math absolute top-[48%] left-[15%] text-slate-400 text-4xl">📝</div>
        <div class="floating-math absolute top-[78%] right-[45%] text-amber-700 font-mono text-lg font-bold">Fe + CuSO₄ → FeSO₄ + Cu</div>
    </div>

    <header class="border-b border-gray-300 backdrop-blur-md sticky top-0 z-50 bg-[#FAF9F5]/90 shadow-xs">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center space-x-3 cursor-pointer" onclick="scrollToSection('hero')">
                <div class="bg-[#0052FF] p-2 rounded-xl text-white shadow-md shadow-blue-500/30 transition hover:scale-105">
                    <i data-lucide="brain-circuit" class="w-5 h-5"></i>
                </div>
                <span class="font-title text-xl font-black tracking-tight text-[#121316]">Домашка.<span class="text-[#0052FF]">AI</span></span>
            </div>
            <nav class="hidden md:flex space-x-8 text-sm font-bold text-gray-600">
                <a href="#features" class="hover:text-[#0052FF] transition-colors">Родителям</a>
                <a href="#students" class="hover:text-[#BE123C] transition-colors">Ученикам</a>
                <a href="#reviews" class="hover:text-[#0052FF] transition-colors">Отзывы</a>
                <a href="#pricing" class="hover:text-[#BE123C] transition-colors">Тарифы</a>
            </nav>
            <div class="flex items-center space-x-4">
                <button onclick="openModal('lk-modal')" class="text-xs font-bold text-gray-800 hover:text-white transition flex items-center space-x-2 border-2 border-[#121316] px-4 py-2 rounded-xl bg-white hover:bg-[#121316] shadow-sm active:scale-97">
                    <i data-lucide="user" class="w-4 h-4"></i>
                    <span>Личный кабинет</span>
                </button>
            </div>
        </div>
    </header>

    <main class="relative z-10">
        
        <section id="hero" class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-16 pb-16 text-center relative">
            <div class="animate-fade-up inline-flex items-center space-x-2 bg-[#0052FF]/10 border-2 border-[#0052FF]/30 text-[#0052FF] px-4 py-1.5 rounded-full text-xs font-bold mb-8 shadow-xs">
                <span class="w-2 h-2 rounded-full bg-[#BE123C] animate-pulse"></span>
                <span>Мгновенное Vision API распознавание формул и текстов</span>
            </div>
            
            <h1 class="animate-fade-up delay-1 hero-title text-3xl sm:text-5xl lg:text-[3.25rem] xl:text-6xl text-[#121316] max-w-5xl mx-auto">
                <span class="line">Твой личный <span class="text-[#0052FF] underline decoration-[#BE123C] decoration-4 underline-offset-[6px]">ИИ-репетитор</span></span>
                <span class="line">на экране <span class="text-[#BE123C]">смартфона</span></span>
            </h1>
            
            <p class="animate-fade-up delay-2 hero-subtitle mt-10 text-lg sm:text-xl lg:text-2xl text-gray-700 max-w-3xl mx-auto font-medium">
                Мы не просто даем списать — <span class="text-[#0052FF] font-bold border-b-3 border-[#BE123C]">мы подробно объясняем</span> логику каждого действия!
            </p>

            <div class="animate-fade-up delay-3 mt-12 max-w-3xl mx-auto bg-white border-2 border-gray-300 rounded-3xl p-6 shadow-xl shadow-gray-300/50 relative overflow-hidden">
                
                <div id="laser-scanner" class="hidden scanner-line"></div>

                <div class="flex flex-wrap items-center justify-between border-b-2 border-gray-100 pb-4 mb-6 gap-4 relative z-10">
                    <div class="flex flex-wrap items-center gap-4 text-xs font-bold">
                        <div class="flex items-center space-x-2 text-gray-700">
                            <i data-lucide="book-open" class="w-4 h-4 text-[#BE123C]"></i>
                            <span>Предмет:</span>
                            <select id="widget-subject-select" class="bg-gray-100 border-2 border-gray-300 rounded-xl px-2.5 py-1.5 text-[#121316] focus:outline-none focus:border-[#0052FF] font-bold transition-all hover:bg-gray-200 cursor-pointer">
                                <option value="math">📐 Математика</option>
                                <option value="rus">📝 Русский язык</option>
                                <option value="eng">🇬🇧 Английский язык</option>
                                <option value="physics">⚡ Физика</option>
                                <option value="social">👥 Обществознание</option>
                                <option value="chemistry">🧪 Химия</option>
                                <option value="inf">💻 Информатика</option>
                            </select>
                        </div>
                        <div class="flex items-center space-x-2 text-gray-700">
                            <i data-lucide="sliders" class="w-4 h-4 text-[#0052FF]"></i>
                            <span>Режим разбора:</span>
                            <select id="age-mode" class="bg-gray-100 border-2 border-gray-300 rounded-xl px-2.5 py-1.5 text-[#121316] focus:outline-none focus:border-[#0052FF] font-bold transition-all hover:bg-gray-200 cursor-pointer">
                                <option value="5">Поясни как в 5 классе</option>
                                <option value="9">Поясни как в 9 классе</option>
                                <option value="ege" selected>Уровень ОГЭ / ЕГЭ</option>
                            </select>
                        </div>
                    </div>
                    <div class="flex items-center space-x-1 bg-gray-100 p-1 rounded-xl border-2 border-gray-200 text-xs font-bold">
                        <button onclick="switchTab('photo-tab')" id="btn-photo-tab" class="px-4 py-2 rounded-lg bg-white text-[#121316] shadow-xs border border-gray-200 transition-all duration-200 cursor-pointer">Скриншот / Фото</button>
                        <button onclick="switchTab('text-tab')" id="btn-text-tab" class="px-4 py-2 rounded-lg text-gray-500 hover:text-[#121316] transition-all duration-200 cursor-pointer">Вручную</button>
                    </div>
                </div>

                <div id="photo-tab" class="space-y-4 relative z-10">
                    <div class="border-2 border-dashed border-gray-300 hover:border-[#0052FF] rounded-2xl p-8 transition-all duration-300 cursor-pointer bg-gray-50/50 relative group hover:bg-white shadow-xs" onclick="document.getElementById('file-input').click()">
                        <input type="file" id="file-input" accept="image/*" class="hidden" onchange="handleFileUpload(event)">
                        <div class="flex flex-col items-center justify-center space-y-3">
                            <div class="p-4 bg-white rounded-full border-2 border-gray-200 group-hover:scale-110 group-hover:border-[#0052FF] transition-all duration-300 text-gray-400 group-hover:text-[#0052FF] shadow-sm">
                                <i data-lucide="camera" class="w-8 h-8"></i>
                            </div>
                            <p class="text-sm text-gray-800 font-bold group-hover:text-[#0052FF] transition-colors">Сделайте снимок домашней работы или прикрепите скриншот</p>
                            <p class="text-xs text-gray-400 font-medium">Распознавание формул, графиков и рукописных тетрадей в реальном времени</p>
                        </div>
                    </div>
                </div>

                <div id="text-tab" class="space-y-4 hidden relative z-10">
                    <textarea id="manual-text" rows="4" class="w-full bg-gray-50/50 border-2 border-gray-200 rounded-2xl p-4 text-sm text-[#121316] font-medium placeholder-gray-400 focus:outline-none focus:border-[#0052FF] focus:bg-white transition-all" placeholder="Введите текст вопроса, математическую матрицу или химическую реакцию вручную..."></textarea>
                    <button onclick="processVisionAPI('text')" class="w-full bg-[#0052FF] hover:bg-[#0040D0] text-white font-bold text-sm py-3.5 rounded-xl transition-all shadow-md shadow-blue-600/20 active:scale-99 flex items-center justify-center space-x-2 cursor-pointer group">
                        <i data-lucide="sparkles" class="w-4 h-4 group-hover:rotate-12 transition-transform"></i>
                        <span>Распознать и сгенерировать пошаговое объяснение</span>
                    </button>
                </div>

                <div id="ai-loading" class="hidden py-8 flex flex-col items-center justify-center space-y-3 relative z-10">
                    <div class="relative w-12 h-12">
                        <div class="absolute inset-0 border-4 border-blue-100 rounded-full"></div>
                        <div class="absolute inset-0 border-4 border-t-[#0052FF] rounded-full animate-spin"></div>
                    </div>
                    <p class="text-sm text-[#0052FF] font-bold animate-pulse tracking-wide">Vision API считывает структуру данных...</p>
                </div>

                <div id="ai-result" class="hidden border-t-2 border-gray-100 pt-6 mt-6 text-left space-y-4 relative z-10">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-2 text-emerald-600 text-xs font-bold">
                            <i data-lucide="check-circle" class="w-4 h-4"></i>
                            <span>Интеллектуальный разбор успешно построен</span>
                        </div>
                        <button onclick="saveToHistory()" class="text-xs font-bold text-gray-600 hover:text-[#121316] transition-all flex items-center space-x-1 border-2 border-gray-200 px-3 py-1.5 rounded-xl bg-white shadow-xs active:scale-95 cursor-pointer">
                            <i data-lucide="bookmark" class="w-3.5 h-3.5 text-gray-400"></i>
                            <span>Сохранить в историю задач</span>
                        </button>
                    </div>
                    <div class="bg-gray-50 rounded-2xl p-4 border-2 border-gray-200 font-mono text-xs text-gray-800">
                        <span class="text-gray-400 block mb-1 font-sans font-bold">// Сканированный ИИ материал:</span>
                        <p id="detected-text">...</p>
                    </div>
                    <div class="space-y-3" id="explanation-steps"></div>
                </div>
            </div>

            <p class="mt-16 font-title text-lg sm:text-xl font-bold text-gray-700 max-w-4xl mx-auto">
                Поддержка в сфере образования на основе искусственного интеллекта по запросу.
            </p>
        </section>

        <section id="features" class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 border-t-2 border-gray-200">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
                <div class="lg:col-span-7 space-y-5">
                    <div class="text-[10px] font-black tracking-wider text-rose-800 uppercase bg-rose-100 border-2 border-rose-200 px-3 py-1 rounded-full inline-block">
                        Родительский контроль и спокойствие
                    </div>
                    <h2 class="font-title section-title text-2xl sm:text-3xl lg:text-4xl font-black text-[#121316]">
                        Превратите домашние задания в <span class="text-[#0052FF]">дружеские рукопожатия</span>.
                    </h2>
                    <p class="text-gray-600 prose-spacing text-base font-medium">
                        Введите вопрос из домашнего задания и получите мгновенную помощь. Как и хороший репетитор, <span class="text-[#BE123C] font-bold">Khanmigo</span> мягко направляет ребенка, чтобы тот сам находил ответы.
                    </p>
                    <div class="pt-2">
                        <button onclick="openModal('auth-modal')" class="bg-[#121316] hover:bg-[#0052FF] text-white font-bold text-xs px-8 py-4 rounded-xl transition-all duration-200 shadow-md active:scale-97 tracking-wide cursor-pointer">
                            РЕГИСТРИРУЙТЕСЬ БЕСПЛАТНО
                        </button>
                    </div>
                </div>
                <div class="lg:col-span-5 bg-gradient-to-br from-white to-gray-50 border-2 border-gray-300 rounded-3xl p-6 shadow-sm">
                    <h4 class="text-xs font-bold text-gray-800 mb-4 flex items-center space-x-2">
                        <i data-lucide="help-circle" class="w-4 h-4 text-[#BE123C]"></i>
                        <span>Точечное устранение болей родителей 40+</span>
                    </h4>
                    <ul class="space-y-3.5 text-xs font-medium text-gray-600">
                        <li class="flex items-start space-x-2.5">
                            <i data-lucide="check" class="w-4 h-4 text-emerald-600 shrink-0 mt-0.5 border border-emerald-200 rounded-full bg-emerald-50"></i>
                            <span>**Для занятых мам и пап**: Больше не нужно ломать голову над комплексными формулами и уравнениями поздним вечером.</span>
                        </li>
                        <li class="flex items-start space-x-2.5">
                            <i data-lucide="check" class="w-4 h-4 text-emerald-600 shrink-0 mt-0.5 border border-emerald-200 rounded-full bg-emerald-50"></i>
                            <span>**Разумные траты**: Традиционный репетитор стоит от 1500 ₽ за час. Зачем покупать абонемент, если нужно просто и внятно объяснить одну сложную задачу прямо сейчас?</span>
                        </li>
                    </ul>
                </div>
            </div>
        </section>

        <section id="students" class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 border-t-2 border-gray-200">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
                <div class="lg:col-span-5 order-last lg:order-first bg-white border-2 border-gray-300 rounded-3xl p-6 shadow-sm">
                    <div class="grid grid-cols-2 gap-2 text-center text-xs font-bold text-gray-800">
                        <div class="bg-gray-50 p-3 rounded-xl border border-gray-200 transition-all hover:bg-blue-50/50 hover:border-[#0052FF]">📐 Математика</div>
                        <div class="bg-gray-50 p-3 rounded-xl border border-gray-200 transition-all hover:bg-blue-50/50 hover:border-[#0052FF]">📝 Русский язык</div>
                        <div class="bg-gray-50 p-3 rounded-xl border border-gray-200 transition-all hover:bg-blue-50/50 hover:border-[#0052FF]">🇬🇧 Английский</div>
                        <div class="bg-gray-50 p-3 rounded-xl border border-gray-200 transition-all hover:bg-blue-50/50 hover:border-[#0052FF]">⚡ Физика</div>
                        <div class="bg-gray-50 p-3 rounded-xl border border-gray-200 transition-all hover:bg-blue-50/50 hover:border-[#0052FF]">👥 Общага</div>
                        <div class="bg-gray-50 p-3 rounded-xl border border-gray-200 transition-all hover:bg-blue-50/50 hover:border-[#0052FF]">🧪 Химия</div>
                    </div>
                </div>
                <div class="lg:col-span-7 space-y-5">
                    <div class="text-[10px] font-black tracking-wider text-[#0052FF] uppercase bg-blue-100 border-2 border-blue-200 px-3 py-1 rounded-full inline-block">
                        Развитие силы интеллекта
                    </div>
                    <h2 class="font-title section-title text-2xl sm:text-3xl lg:text-4xl font-black text-[#121316]">
                        Развивайте силу своего <span class="text-[#BE123C]">мозга</span>.
                    </h2>
                    <p class="text-gray-600 prose-spacing text-base font-medium">
                        Платформа <span class="text-[#0052FF] font-bold">побуждает вас мыслить критически</span> и успешно решать комплексные задачи, фундаментально не предоставляя готовых прямых ответов для банального списывания. Изучайте новые дисциплины в любое удобное время, будь то сложная алгебра, подготовка к ОГЭ/ЕГЭ, формулы по химии, обществознание или написание эссе.
                    </p>
                    <div class="pt-2">
                        <button onclick="openModal('auth-modal')" class="bg-[#121316] hover:bg-[#BE123C] text-white font-bold text-xs px-8 py-4 rounded-xl transition-all duration-200 shadow-md active:scale-97 tracking-wide cursor-pointer">
                            РЕГИСТРИРУЙТЕСЬ БЕСПЛАТНО
                        </button>
                    </div>
                </div>
            </div>
        </section>

        <section id="reviews" class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 border-t-2 border-gray-200">
            <div class="text-center max-w-3xl mx-auto mb-12">
                <h2 class="font-title section-title text-xl sm:text-3xl font-black text-[#121316]">Ученики и родители оценили Домашка.AI</h2>
                <p class="text-sm font-bold text-gray-500 mt-2">Разбор в одном окне, реальное понимание сложных тем и колоссальная экономия бюджета</p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div class="bg-white border-2 border-gray-200 p-6 rounded-2xl flex flex-col justify-between shadow-xs hover:shadow-md transition-all duration-300">
                    <p class="text-gray-700 text-xs leading-relaxed font-medium italic">
                        «Поразило, насколько всё удобно устроено в одном окне. Сделали снимок тетрадки по химии, ИИ распознал формулу реакции и выдал пошаговый разбор, объясняя абсолютно всё подробно и понятно. Репетиторы стоят гораздо дороже, это невероятная экономия времени и денег!»
                    </p>
                    <div class="mt-6 flex items-center space-x-3 pt-4 border-t border-gray-100">
                        <div class="w-10 h-10 bg-blue-100 text-[#0052FF] rounded-full flex items-center justify-center font-bold text-xs border-2 border-blue-200">АН</div>
                        <div>
                            <h5 class="text-xs font-bold text-[#121316]">Анна Н. (Мама школьника)</h5>
                            <span class="text-[10px] font-bold text-gray-400">Пакет «Точечный удар»</span>
                        </div>
                    </div>
                </div>
                <div class="bg-white border-2 border-gray-200 p-6 rounded-2xl flex flex-col justify-between shadow-xs hover:shadow-md transition-all duration-300">
                    <p class="text-gray-700 text-xs leading-relaxed font-medium italic">
                        «Готовлюсь к ЕГЭ по физике и информатике. Обычные решебники просто пишут ответ, списываешь и ничего не понимаешь, а у доски заваливают. Домашка.AI расписывает логику так, словно сидишь с крутым учителем один на один. Очень выручает!»
                    </p>
                    <div class="mt-6 flex items-center space-x-3 pt-4 border-t border-gray-100">
                        <div class="w-10 h-10 bg-purple-100 text-purple-600 rounded-full flex items-center justify-center font-bold text-xs border-2 border-purple-200">КЛ</div>
                        <div>
                            <h5 class="text-xs font-bold text-[#121316]">Кирилл Л. (11 класс)</h5>
                            <span class="text-[10px] font-bold text-gray-400">Готовится к профильным экзаменам</span>
                        </div>
                    </div>
                </div>
                <div class="bg-white border-2 border-gray-200 p-6 rounded-2xl flex flex-col justify-between shadow-xs hover:shadow-md transition-all duration-300">
                    <p class="text-gray-700 text-xs leading-relaxed font-medium italic">
                        «Для многодетной семьи подписка "Всё включено" — это спасение. Младший разбирает математику и русский за 5 класс, старшая готовится к обществознанию. Объяснения адаптируются под возраст идеально. Больше никаких ночных споров над уроками!»
                    </p>
                    <div class="mt-6 flex items-center space-x-3 pt-4 border-t border-gray-100">
                        <div class="w-10 h-10 bg-rose-100 text-[#BE123C] rounded-full flex items-center justify-center font-bold text-xs border-2 border-rose-200">ИВ</div>
                        <div>
                            <h5 class="text-xs font-bold text-[#121316]">Ирина В. (Мама троих детей)</h5>
                            <span class="text-[10px] font-bold text-gray-400">Сэкономила более 12 000 ₽ за месяц</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section id="pricing" class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 border-t-2 border-gray-200 relative">
            <div class="text-center max-w-3xl mx-auto mb-12">
                <div class="text-[10px] font-black tracking-wider text-emerald-800 uppercase bg-emerald-100 border-2 border-emerald-200 px-3 py-1 rounded-full inline-block mb-3">Гибкое управление подпиской</div>
                <h2 class="font-title section-title text-2xl sm:text-3xl font-black text-[#121316]">Умные тарифы для любых задач</h2>
                <p class="text-sm font-bold text-gray-500 mt-2">Каждый тариф включает 1 день бесплатного тест-драйва. Без скрытых платежей.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto items-stretch">
                
                <div class="bg-white border-2 border-gray-300 rounded-3xl p-6 flex flex-col justify-between hover:border-gray-400 transition-all duration-300 relative shadow-xs hover:shadow-md">
                    <div>
                        <div class="flex justify-between items-start">
                            <h4 class="text-sm font-black text-[#121316]">Точечный удар</h4>
                            <span class="bg-gray-100 text-gray-500 text-[9px] uppercase font-bold px-2 py-0.5 rounded border border-gray-200">1 предмет</span>
                        </div>
                        <p class="text-xs text-gray-500 mt-2 font-medium italic">Для кого: Мама поняла, что у ребенка западают только уравнения по химии.</p>
                        <div class="mt-4 flex items-baseline">
                            <span class="text-3xl font-black text-[#121316] font-title">590 ₽</span>
                            <span class="text-xs font-bold text-gray-400 ml-1">/ мес.</span>
                        </div>
                        
                        <div class="mt-6 pt-4 border-t border-gray-100">
                            <label class="block text-[11px] font-bold text-gray-500 mb-2.5 flex justify-between">
                                <span>Выберите предмет подписки:</span>
                                <span class="text-[#0052FF]">Шаг 1 из 1</span>
                            </label>
                            <div class="space-y-1.5" id="tariff-1-group">
                                <label class="flex items-center space-x-2.5 text-xs font-bold text-gray-700 bg-gray-50/50 px-3 py-2 rounded-xl cursor-pointer border border-gray-200 hover:border-[#0052FF] hover:bg-white transition-all">
                                    <input type="radio" name="single-subject" value="Математика" checked class="text-[#0052FF] focus:ring-0">
                                    <span>📐 Математика</span>
                                </label>
                                <label class="flex items-center space-x-2.5 text-xs font-bold text-gray-700 bg-gray-50/50 px-3 py-2 rounded-xl cursor-pointer border border-gray-200 hover:border-[#0052FF] hover:bg-white transition-all">
                                    <input type="radio" name="single-subject" value="Русский язык" class="text-[#0052FF] focus:ring-0">
                                    <span>📝 Русский язык</span>
                                </label>
                                <label class="flex items-center space-x-2.5 text-xs font-bold text-gray-700 bg-gray-50/50 px-3 py-2 rounded-xl cursor-pointer border border-gray-200 hover:border-[#0052FF] hover:bg-white transition-all">
                                    <input type="radio" name="single-subject" value="Английский язык" class="text-[#0052FF] focus:ring-0">
                                    <span>🇬🇧 Английский язык</span>
                                </label>
                                <label class="flex items-center space-x-2.5 text-xs font-bold text-gray-700 bg-gray-50/50 px-3 py-2 rounded-xl cursor-pointer border border-gray-200 hover:border-[#0052FF] hover:bg-white transition-all">
                                    <input type="radio" name="single-subject" value="Физика" class="text-[#0052FF] focus:ring-0">
                                    <span>⚡ Физика</span>
                                </label>
                                <label class="flex items-center space-x-2.5 text-xs font-bold text-gray-700 bg-gray-50/50 px-3 py-2 rounded-xl cursor-pointer border border-gray-200 hover:border-[#0052FF] hover:bg-white transition-all">
                                    <input type="radio" name="single-subject" value="Обществознание" class="text-[#0052FF] focus:ring-0">
                                    <span>👥 Обществознание</span>
                                </label>
                                <label class="flex items-center space-x-2.5 text-xs font-bold text-gray-700 bg-gray-50/50 px-3 py-2 rounded-xl cursor-pointer border border-gray-200 hover:border-[#0052FF] hover:bg-white transition-all">
                                    <input type="radio" name="single-subject" value="Химия" class="text-[#0052FF] focus:ring-0">
                                    <span>🧪 Химия</span>
                                </label>
                                <label class="flex items-center space-x-2.5 text-xs font-bold text-gray-700 bg-gray-50/50 px-3 py-2 rounded-xl cursor-pointer border border-gray-200 hover:border-[#0052FF] hover:bg-white transition-all">
                                    <input type="radio" name="single-subject" value="Информатика" class="text-[#0052FF] focus:ring-0">
                                    <span>💻 Информатика</span>
                                </label>
                            </div>
                        </div>
                    </div>
                    <button onclick="checkoutSingleSubject()" class="w-full mt-6 bg-[#121316] hover:bg-[#0052FF] text-white font-bold text-xs py-3.5 rounded-xl transition-all cursor-pointer active:scale-98 shadow-sm">ЗАРЕГИСТРИРУЙТЕСЬ БЕСПЛАТНО</button>
                </div>

                <div class="bg-white border-2 border-[#0052FF] rounded-3xl p-6 flex flex-col justify-between relative shadow-xl shadow-blue-500/10 hover:shadow-blue-500/20 transition-all duration-300">
                    <div class="absolute -top-3 left-1/2 -translate-x-1/2 bg-[#0052FF] text-white text-[9px] font-black px-3 py-1 rounded-full tracking-wider animate-pulse">ВЫБОР ПРОФИЛЯ</div>
                    <div>
                        <div class="flex justify-between items-start">
                            <h4 class="text-sm font-black text-[#121316]">Предметный Буст</h4>
                            <span class="text-[#0052FF] text-xs font-black">3 предмета</span>
                        </div>
                        <p class="text-xs text-gray-500 mt-2 font-medium italic">Для кого: Школьник сдает ОГЭ/ЕГЭ по выбранному профилю. Пользователь сам выбирает 3 галочки из списка.</p>
                        <div class="mt-4 flex items-baseline">
                            <span class="text-4xl font-black text-[#121316] font-title">1 050 ₽</span>
                            <span class="text-xs font-bold text-gray-400 ml-1">/ мес.</span>
                        </div>
                        
                        <div class="mt-6 pt-4 border-t-2 border-blue-100">
                            <label class="block text-[11px] font-bold text-[#0052FF] mb-2 flex justify-between">
                                <span>Выберите ровно 3 предмета:</span>
                                <span id="boost-counter" class="font-bold text-[#BE123C] bg-rose-50 px-2 py-0.5 rounded border border-rose-100">0 из 3</span>
                            </label>
                            <div class="space-y-1.5">
                                <label class="flex items-center space-x-2.5 text-xs font-bold text-gray-700 bg-gray-50/50 px-3 py-2 rounded-xl cursor-pointer border border-gray-200 hover:border-[#0052FF] hover:bg-white transition-all">
                                    <input type="checkbox" name="boost-subject" value="Математика" onchange="updateBoostCounter()" class="rounded border-gray-300 text-[#0052FF] focus:ring-0">
                                    <span>📐 Математика</span>
                                </label>
                                <label class="flex items-center space-x-2.5 text-xs font-bold text-gray-700 bg-gray-50/50 px-3 py-2 rounded-xl cursor-pointer border border-gray-200 hover:border-[#0052FF] hover:bg-white transition-all">
                                    <input type="checkbox" name="boost-subject" value="Русский язык" onchange="updateBoostCounter()" class="rounded border-gray-300 text-[#0052FF] focus:ring-0">
                                    <span>📝 Русский язык</span>
                                </label>
                                <label class="flex items-center space-x-2.5 text-xs font-bold text-gray-700 bg-gray-50/50 px-3 py-2 rounded-xl cursor-pointer border border-gray-200 hover:border-[#0052FF] hover:bg-white transition-all">
                                    <input type="checkbox" name="boost-subject" value="Английский язык" onchange="updateBoostCounter()" class="rounded border-gray-300 text-[#0052FF] focus:ring-0">
                                    <span>🇬🇧 Английский язык</span>
                                </label>
                                <label class="flex items-center space-x-2.5 text-xs font-bold text-gray-700 bg-gray-50/50 px-3 py-2 rounded-xl cursor-pointer border border-gray-200 hover:border-[#0052FF] hover:bg-white transition-all">
                                    <input type="checkbox" name="boost-subject" value="Физика" onchange="updateBoostCounter()" class="rounded border-gray-300 text-[#0052FF] focus:ring-0">
                                    <span>⚡ Физика</span>
                                </label>
                                <label class="flex items-center space-x-2.5 text-xs font-bold text-gray-700 bg-gray-50/50 px-3 py-2 rounded-xl cursor-pointer border border-gray-200 hover:border-[#0052FF] hover:bg-white transition-all">
                                    <input type="checkbox" name="boost-subject" value="Обществознание" onchange="updateBoostCounter()" class="rounded border-gray-300 text-[#0052FF] focus:ring-0">
                                    <span>👥 Обществознание</span>
                                </label>
                                <label class="flex items-center space-x-2.5 text-xs font-bold text-gray-700 bg-gray-50/50 px-3 py-2 rounded-xl cursor-pointer border border-gray-200 hover:border-[#0052FF] hover:bg-white transition-all">
                                    <input type="checkbox" name="boost-subject" value="Химия" onchange="updateBoostCounter()" class="rounded border-gray-300 text-[#0052FF] focus:ring-0">
                                    <span>🧪 Химия</span>
                                </label>
                                <label class="flex items-center space-x-2.5 text-xs font-bold text-gray-700 bg-gray-50/50 px-3 py-2 rounded-xl cursor-pointer border border-gray-200 hover:border-[#0052FF] hover:bg-white transition-all">
                                    <input type="checkbox" name="boost-subject" value="Информатика" onchange="updateBoostCounter()" class="rounded border-gray-300 text-[#0052FF] focus:ring-0">
                                    <span>💻 Информатика</span>
                                </label>
                            </div>
                        </div>
                    </div>
                    <button id="btn-boost-buy" disabled onclick="checkoutBoostSubjects()" class="w-full mt-6 bg-gray-200 opacity-50 pointer-events-none text-gray-400 font-bold text-xs py-3.5 rounded-xl transition-all duration-350">ЗАРЕГИСТРИРУЙТЕСЬ БЕСПЛАТНО</button>
                </div>

                <div class="bg-white border-2 border-gray-300 rounded-3xl p-6 flex flex-col justify-between hover:border-gray-400 transition-all duration-300 shadow-xs hover:shadow-md">
                    <div>
                        <div class="flex justify-between items-start">
                            <h4 class="text-sm font-black text-[#121316]">Всё включено</h4>
                            <span class="bg-emerald-50 text-emerald-700 text-[9px] uppercase font-bold px-2 py-0.5 rounded border border-emerald-200">Максимум</span>
                        </div>
                        <p class="text-xs text-gray-500 mt-2 font-medium italic">Для кого: Для ленивых или многодетных родителей. Снимает любые ограничения. Самый маржинальный тариф.</p>
                        <div class="mt-4 flex items-baseline">
                            <span class="text-3xl font-black text-[#121316] font-title">1 490 ₽</span>
                            <span class="text-xs font-bold text-gray-400 ml-1">/ мес.</span>
                        </div>
                        
                        <div class="mt-6 pt-4 border-t border-gray-100 space-y-2">
                            <label class="block text-[11px] font-bold text-emerald-700 mb-2">Все 7 предметов разблокированы:</label>
                            <div class="grid grid-cols-1 gap-1.5 text-xs font-bold text-gray-700">
                                <div class="flex items-center space-x-2 bg-gray-50 border border-gray-150 px-3 py-1.5 rounded-xl"><i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-600 shrink-0"></i><span>📐 Математика</span></div>
                                <div class="flex items-center space-x-2 bg-gray-50 border border-gray-150 px-3 py-1.5 rounded-xl"><i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-600 shrink-0"></i><span>📝 Русский язык</span></div>
                                <div class="flex items-center space-x-2 bg-gray-50 border border-gray-150 px-3 py-1.5 rounded-xl"><i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-600 shrink-0"></i><span>🇬🇧 Английский язык</span></div>
                                <div class="flex items-center space-x-2 bg-gray-50 border border-gray-150 px-3 py-1.5 rounded-xl"><i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-600 shrink-0"></i><span>⚡ Физика</span></div>
                                <div class="flex items-center space-x-2 bg-gray-50 border border-gray-150 px-3 py-1.5 rounded-xl"><i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-600 shrink-0"></i><span>👥 Обществознание</span></div>
                                <div class="flex items-center space-x-2 bg-gray-50 border border-gray-150 px-3 py-1.5 rounded-xl"><i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-600 shrink-0"></i><span>🧪 Химия</span></div>
                                <div class="flex items-center space-x-2 bg-gray-50 border border-gray-150 px-3 py-1.5 rounded-xl"><i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-600 shrink-0"></i><span>💻 Информатика</span></div>
                            </div>
                        </div>
                    </div>
                    <button onclick="checkoutAllInclusive()" class="w-full mt-6 bg-[#121316] hover:bg-[#BE123C] text-white font-bold text-xs py-3.5 rounded-xl transition-all cursor-pointer active:scale-98 shadow-sm">ЗАРЕГИСТРИРУЙТЕСЬ БЕСПЛАТНО</button>
                </div>
            </div>
        </section>

        <section class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-16 text-center">
            <div class="bg-[#121316] border border-gray-800 rounded-3xl p-10 sm:p-14 relative overflow-hidden shadow-xl shadow-gray-900/10">
                <div class="relative z-10 max-w-2xl mx-auto space-y-5">
                    <h2 class="font-title section-title text-xl sm:text-3xl font-black text-white">
                        Попробуйте лучший образовательный инструмент на базе нейросетей
                    </h2>
                    <p class="text-xs text-gray-400 font-medium">
                        Первые 24 часа бесплатного доступа. Настройте родительский кабинет, оцените скорость Vision API и посмотрите историю задач вашего ребенка.
                    </p>
                    <div class="pt-2">
                        <button onclick="scrollToSection('hero')" class="bg-[#0052FF] hover:bg-[#0047D0] text-white font-bold text-xs px-8 py-4 rounded-xl transition-all duration-200 shadow-lg hover:shadow-xl shadow-blue-600/20 active:scale-95 cursor-pointer">
                            ПОПРОБУЙ БЕСПЛАТНО
                        </button>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <footer class="border-t border-gray-200 bg-white py-8 text-[11px] font-bold text-gray-400">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-4">
            <div>&copy; 2026 Домашка.AI. Все права защищены. Разработано для понятного и высокотехнологичного обучения школьников.</div>
            <div class="flex space-x-6">
                <a href="#" class="hover:text-gray-600 transition-colors">Политика конфиденциальности</a>
                <a href="#" class="hover:text-gray-600 transition-colors">Публичная оферта</a>
            </div>
        </div>
    </footer>

    <div id="auth-modal" class="fixed inset-0 z-50 overflow-y-auto hidden bg-black/40 backdrop-blur-xs flex items-center justify-center p-4">
        <div class="bg-white border-2 border-gray-200 w-full max-w-md rounded-2xl p-6 relative shadow-2xl transition-all">
            <button onclick="closeModal('auth-modal')" class="absolute top-4 right-4 text-gray-400 hover:text-gray-700 cursor-pointer"><i data-lucide="x" class="w-4 h-4"></i></button>
            <h3 class="font-title text-base font-black text-[#121316] mb-1">СОЗДАТЬ ПРОФИЛЬ</h3>
            <p class="text-xs font-bold text-gray-400 mb-5">Запустите бесплатные сутки тест-драйва выбранного тарифа.</p>
            <form onsubmit="handleAuth(event)" class="space-y-4">
                <div>
                    <label class="block text-[11px] font-bold text-gray-500 mb-1.5">Кто будет управлять кабинетом:</label>
                    <select class="w-full bg-gray-50 border-2 border-gray-200 rounded-xl px-3 py-2.5 text-xs text-[#121316] focus:outline-none focus:border-[#0052FF] font-bold cursor-pointer">
                        <option value="parent">Родитель (для оплаты и контроля)</option>
                        <option value="student">Ученик / Студент</option>
                    </select>
                </div>
                <div>
                    <label class="block text-[11px] font-bold text-gray-500 mb-1.5">Номер телефона или Email</label>
                    <input type="text" required class="w-full bg-gray-50 border-2 border-gray-200 rounded-xl px-3 py-2.5 text-xs text-[#121316] font-bold placeholder-gray-400 focus:outline-none focus:border-[#0052FF]" placeholder="+7 (999) 000-00-00">
                </div>
                <button type="submit" class="w-full bg-[#0052FF] hover:bg-[#0042D0] text-white font-bold text-xs py-3 rounded-xl transition shadow-md shadow-blue-500/10 cursor-pointer">Активировать бесплатный доступ</button>
            </form>
        </div>
    </div>

    <div id="lk-modal" class="fixed inset-0 z-50 overflow-y-auto hidden bg-black/40 backdrop-blur-xs flex items-center justify-center p-4">
        <div class="bg-white border-2 border-gray-200 w-full max-w-2xl rounded-2xl p-6 relative shadow-2xl transition-all">
            <button onclick="closeModal('lk-modal')" class="absolute top-4 right-4 text-gray-400 hover:text-gray-700 cursor-pointer"><i data-lucide="x" class="w-4 h-4"></i></button>
            
            <div class="flex items-center space-x-3 border-b-2 border-gray-100 pb-4 mb-6">
                <div class="bg-blue-50 border border-blue-200 p-2 rounded-xl text-[#0052FF]"><i data-lucide="shield-check" class="w-5 h-5"></i></div>
                <div>
                    <h3 class="font-title text-sm font-black text-[#121316]">КАБИНЕТ РОДИТЕЛЬСКОГО КОНТРОЛЯ</h3>
                    <p class="text-[10px] font-bold text-gray-400">Мониторинг прогресса обучения, предметов и активности ребенка</p>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-12 gap-6">
                <div class="md:col-span-5 space-y-4 border-r-2 border-gray-100 pr-0 md:pr-6">
                    <div class="bg-gray-50 border-2 border-gray-200 p-4 rounded-xl">
                        <span class="text-[9px] uppercase tracking-wider text-gray-400 block font-bold">Профиль</span>
                        <span class="text-xs font-black text-[#121316] mt-1 block">Елена Николаевна (Мама)</span>
                        <span class="text-[11px] font-bold text-[#0052FF] block mt-0.5">Никита (9 класс)</span>
                    </div>
                    <div class="bg-gray-50 border-2 border-gray-200 p-4 rounded-xl">
                        <span class="text-[9px] uppercase tracking-wider text-gray-400 block font-bold">Статус подписки</span>
                        <span class="text-[10px] bg-amber-50 text-amber-700 px-2 py-0.5 rounded border border-amber-100 inline-block mt-1 font-bold">Тест-драйв (Осталось 23 часа)</span>
                        <button onclick="closeModal('lk-modal'); scrollToSection('pricing')" class="w-full mt-3 bg-[#0052FF] hover:bg-[#0042D0] text-white font-bold text-[10px] py-2 rounded-lg transition cursor-pointer">Продлить доступ</button>
                    </div>
                </div>

                <div class="md:col-span-7 space-y-3">
                    <span class="text-xs font-bold text-gray-500 block mb-1 flex items-center space-x-1.5">
                        <i data-lucide="history" class="w-3.5 h-3.5 text-[#0052FF]"></i>
                        <span>История недавних задач ребенка:</span>
                    </span>
                    <div class="space-y-2 max-h-56 overflow-y-auto pr-1" id="history-list">
                        <div class="bg-gray-50 border border-gray-200 p-3 rounded-xl text-xs space-y-1">
                            <div class="flex justify-between text-[9px] text-gray-400">
                                <span>Химия • Уровень 9 класса</span>
                                <span>Сегодня, 19:12</span>
                            </div>
                            <p class="text-gray-700 font-mono truncate font-bold">Al + O₂ → Al₂O₃. Помоги расставить коэффициенты.</p>
                            <span class="text-emerald-600 text-[10px] font-bold block">✓ Логика темы успешно изучена и закрыта</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        lucide.createIcons();

        function scrollToSection(id) {
            const el = document.getElementById(id);
            if(el) el.scrollIntoView({ behavior: 'smooth' });
        }

        function switchTab(tabId) {
            if(tabId === 'photo-tab') {
                document.getElementById('photo-tab').classList.remove('hidden');
                document.getElementById('text-tab').classList.add('hidden');
                document.getElementById('btn-photo-tab').className = "px-4 py-2 rounded-lg bg-white text-[#121316] shadow-xs border border-gray-200 transition-all cursor-pointer";
                document.getElementById('btn-text-tab').className = "px-4 py-2 rounded-lg text-gray-500 hover:text-[#121316] transition-all cursor-pointer";
            } else {
                document.getElementById('photo-tab').className = "hidden";
                document.getElementById('text-tab').classList.remove('hidden');
                document.getElementById('btn-photo-tab').className = "px-4 py-2 rounded-lg text-gray-500 hover:text-[#121316] transition-all cursor-pointer";
                document.getElementById('btn-text-tab').className = "px-4 py-2 rounded-lg bg-white text-[#121316] shadow-xs border border-gray-200 transition-all cursor-pointer";
            }
        }

        function openModal(id) { document.getElementById(id).classList.remove('hidden'); }
        function closeModal(id) { document.getElementById(id).classList.add('hidden'); }

        function handleFileUpload(event) {
            if(event.target.files && event.target.files[0]) {
                processVisionAPI('image');
            }
        }

        // ОБНОВЛЕННЫЙ ИНТЕРАКТИВНЫЙ СЧЕТЧИК ЧЕКБОКСОВ ПОД СЕМЬ ПРЕДМЕТОВ
        function updateBoostCounter() {
            const checkboxes = document.querySelectorAll('input[name="boost-subject"]:checked');
            const count = checkboxes.length;
            const counterLabel = document.getElementById('boost-counter');
            const buyButton = document.getElementById('btn-boost-buy');

            counterLabel.innerText = `${count} из 3`;

            if (count === 3) {
                counterLabel.className = "font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200 shadow-xs";
                buyButton.removeAttribute('disabled');
                buyButton.className = "w-full mt-6 bg-[#0052FF] hover:bg-[#0042D0] text-white font-bold text-xs py-3.5 rounded-xl transition shadow-lg shadow-blue-500/20 cursor-pointer opacity-100 pointer-events-auto active:scale-98";
            } else {
                counterLabel.className = "font-bold text-[#BE123C] bg-rose-50 px-2 py-0.5 rounded border border-rose-100";
                buyButton.setAttribute('disabled', 'true');
                buyButton.className = "w-full mt-6 bg-gray-200 opacity-50 pointer-events-none text-gray-400 font-bold text-xs py-3.5 rounded-xl transition";
            }
        }

        function checkoutSingleSubject() {
            const subject = document.querySelector('input[name="single-subject"]:checked').value;
            alert(`Вы выбрали тариф «Точечный удар» на предмет: ${subject}.\nАктивирован бесплатный тест-драйв на 24 часа.`);
            openModal('auth-modal');
        }

        function checkoutBoostSubjects() {
            const checkedBoxes = document.querySelectorAll('input[name="boost-subject"]:checked');
            let chosen = [];
            checkedBoxes.forEach(cb => chosen.push(cb.value));
            alert(`Успешно! Вы собрали индивидуальный пакет из 3 предметов: ${chosen.join(', ')}.\nЗапускаем бесплатный тест-драйв.`);
            openModal('auth-modal');
        }

        function checkoutAllInclusive() {
            alert('Вы выбрали тариф «Всё включено» (все 7 профильных предметов).\nЗапускаем бесплатный тест-драйв на 24 часа.');
            openModal('auth-modal');
        }

        // РАБОТА ИИ-ВИДЖЕТА И СТРОГОЕ ОПРЕДЕЛЕНИЕ СЕМИ ПРЕДМЕТОВ
        function processVisionAPI(sourceType) {
            const currentSub = document.getElementById('widget-subject-select').value;
            const ageMode = document.getElementById('age-mode').value;
            
            document.getElementById('photo-tab').classList.add('hidden');
            document.getElementById('text-tab').classList.add('hidden');
            document.getElementById('ai-result').classList.add('hidden');
            
            document.getElementById('laser-scanner').classList.remove('hidden');
            document.getElementById('ai-loading').classList.remove('hidden');

            let detectedTextStr = "2x² - 5x + 2 = 0";
            if(currentSub === 'physics') detectedTextStr = "Определите силу тока в проводнике сопротивлением 10 Ом при напряжении 220 В.";
            if(currentSub === 'chemistry') detectedTextStr = "Расставьте коэффициенты в уравнении реакции: Al + O₂ → Al₂O₃";
            if(currentSub === 'rus') detectedTextStr = "Выполните синтаксический разбор предложения: Нейросети стремительно меняют мир.";
            if(currentSub === 'eng') detectedTextStr = "Translate to English: Вчера я закончил делать сложную домашнюю работу по математике.";
            if(currentSub === 'social') detectedTextStr = "Назовите три основных фактора производства и проиллюстрируйте их примерами.";
            if(currentSub === 'inf') detectedTextStr = "В языке запросов поискового сервера для обозначения логической операции «ИЛИ» используется символ...";

            if(sourceType === 'text') {
                const val = document.getElementById('manual-text').value.trim();
                if(val) detectedTextStr = val;
            }

            setTimeout(() => {
                document.getElementById('laser-scanner').classList.add('hidden');
                document.getElementById('ai-loading').classList.add('hidden');
                document.getElementById('ai-result').classList.remove('hidden');
                document.getElementById('detected-text').innerText = detectedTextStr;
                
                const stepsContainer = document.getElementById('explanation-steps');
                stepsContainer.innerHTML = ''; 

                let steps = [
                    { t: "Шаг 1: Детальный разбор условий задания", d: `ИИ успешно расшифровал контекст по дисциплине [${currentSub.toUpperCase()}]. Фиксируем исходные параметры.` },
                    { t: "Шаг 2: Выделение ключевых формул и правил", d: "Мы не даем списать готовый пустой ответ, а мягко ведем к глубокому усвоению материала. Применяем фундаментальную теорию..." },
                    { t: "Шаг 3: Пошаговое вычисление и логический итог", d: `Пояснение адаптировано под выбранный режим [${ageMode === '5' ? '5 класс' : ageMode === '9' ? '9 класс' : 'ОГЭ/ЕГЭ'}]. Ребенок самостоятельно приходит к правильному решению.` }
                ];

                steps.forEach((step, i) => {
                    const block = document.createElement('div');
                    block.className = "bg-white border-2 border-gray-200 p-4 rounded-xl space-y-1.5 transition-all duration-300 hover:border-[#0052FF]/40 shadow-xs animate-fade-up";
                    block.style.animationDelay = `${i * 0.12}s`;
                    block.innerHTML = `
                        <h5 class="text-xs font-bold text-[#121316] flex items-center space-x-2">
                            <span class="w-5 h-5 rounded-md bg-[#0052FF]/10 text-[#0052FF] text-[10px] flex items-center justify-center font-black border border-[#0052FF]/20">${i+1}</span>
                            <span>${step.t}</span>
                        </h5>
                        <p class="text-xs text-gray-600 leading-relaxed pl-7 font-medium">${step.d}</p>
                    `;
                    stepsContainer.appendChild(block);
                });

            }, 2000);
        }

        function saveToHistory() {
            const taskText = document.getElementById('detected-text').innerText;
            const item = document.createElement('div');
            item.className = "bg-gray-50 border border-gray-200 p-3 rounded-xl text-xs space-y-1 animate-fade-up";
            item.innerHTML = `
                <div class="flex justify-between text-[9px] text-gray-400">
                    <span>Интерактивный разбор</span>
                    <span>Только что</span>
                </div>
                <p class="text-gray-700 font-mono truncate font-bold">${taskText}</p>
                <span class="text-emerald-600 text-[10px] font-bold block">✓ Успешно зафиксировано</span>
            `;
            const list = document.getElementById('history-list');
            list.insertBefore(item, list.firstChild);
            alert('Задача успешно зафиксирована в истории!');
        }

        function handleAuth(e) {
            e.preventDefault();
            alert('Профиль успешно создан! Тестовый доступ на 1 день активирован.');
            closeModal('auth-modal');
            openModal('lk-modal');
        }
    </script>
</body>
</html>"""

OUTPUT.write_text(html_content, encoding="utf-8")
print(f"index.html успешно сгенерирован: {OUTPUT}")