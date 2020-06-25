from app import app

dictionary_words = {
        "Вычислительная машина": "совокупность программных и технических "
                                 "средств, обеспечивающих автоматическое "
                                 "выполнение процессов и обработки информации.",
        "ЦП": "центральный процессор",
        "АЛУ": "арифметико-логическое устрйоство, производит арифмтические и "
               "логические операции.",
        "УУ": "устройство управления - отвечает за управление компонентами "
              "процессора, выборку выборку операций, декодирование их, "
              "синхронизацию",
        "DRAM": "Dynamic RAM - тип энергозависимой полупроводниковой памяти "
                "с произвольным доступом, каждый бит которой хранится в "
                "ячейке, являюзщейся совокупностью конденсатора и "
                "запирающего транзистора",
        "BCD": "Binary-Coded Decimal - форма записи рациональных чисел, "
               "когда каждый десятичный разряд числа записывается в виде его "
               "четырёхбитного двоичного кода",
        "ANSI": "Американский национальный институт стандартов",
        "ISO": "Международная организация по стандартизации",
        "ASCII": "американская стандартная кодировочная таблица для печатных "
                 "символов и некоторых специальных кодов ",
        "UTF": "семейство кодировок Unicode",
        "EBCDIC": "стандартный восьмибитный код, разработанный корпорацией "
                  "IBM для использования на мэйнфреймах собственного "
                  "производства и совместимых с ними. EBCDIC кодирует буквы "
                  "латинского алфавита, арабские цифры, некоторые знаки "
                  "пунктуации и управляющие символы.",
        "SSE1": "SIMD-расширения процессоров Intel. В поздних версиях SSE "
                "можно реализовать, например, умножение векторов за одну "
                "операцию.",
        "SSE2": "SIMD-расширения процессоров Intel. В поздних версиях SSE "
                "можно реализовать, например, умножение векторов за одну "
                "операцию.",
        "SSE3": "SIMD-расширения процессоров Intel. В поздних версиях SSE "
                "можно реализовать, например, умножение векторов за одну "
                "операцию.",
        "SSE4": "SIMD-расширения процессоров Intel. В поздних версиях SSE "
                "можно реализовать, например, умножение векторов за одну "
                "операцию.",
        "MMX": "SIMD-расширения процессоров Intel. В поздних версиях SSE "
               "можно реализовать, например, умножение векторов за одну "
               "операцию.",
        "XXM": "SIMD-расширения процессоров Intel. В поздних версиях SSE "
               "можно реализовать, например, умножение векторов за одну "
               "операцию.",
        "SIMD": "Single Instruction, Multiple Data - параллельная обработка "
                "однотипных данных за одну операцию.",
        "Чипсет": "набор микросхем, спроектированных для совместной работы с "
                  "целью выполнения набора каких-либо функций. Может быть "
                  "разделен на северный и южный мост (пo географическому "
                  "расположению на системной плате)",
        "x86": "архитектура процессора c одноимённым набором команд, впервые "
               "реализованная в процессорах компании Intel (Intel 8086)",
        "x86-64": "64-битное расширение, набор команд, для архитектуры x86, "
                  "разработанное компанией AMD, позволяющее выполнять "
                  "программы в 64-разрядном режиме.",
        "IA-32": "(i386) - Intel Architecture - 32 (alias x86)",
        "IA-64": "64-битная аппаратная платформа: микропроцессорная "
                 "архитектура и соответствующая архитектура набора команд, "
                 "разработанная совместно компаниями Intel и Hewlett "
                 "Packard. Реализована в микропроцессорах Itanium и Itanium "
                 "2. ",
        "ARM": "семейство лицензируемых 32-битных и 64-битных "
               "микропроцессорных ядер разработки компании ARM Limited. "
               "Значимые семейства процессоров: ARM7, ARM9, ARM11 и Cortex. "
               "Используется в мобильных устройствах и не только. ",
        "DMA": "Direct Memory Access - Если контроллер считывает данные из "
               "памяти или записывает их в память без участия центрального "
               "процессора, то говорят, что осуществляется прямой доступ к "
               "памяти",
        "RAM": "Random Access Memory - память произвольного доступа (доступ "
               "к любой ячейке памяти происходит за константное время)",
        "MMU": "Memory Managment Unit - Устроство управления памятью. Его "
               "функции заключаются в трансляции адресов виртуальной памяти "
               "в адреса физической памяти (то есть управление виртуальной "
               "памятью), защите памяти, управлении кеш-памятью, арбитражем "
               "шины. Содержит два подустройств - Segment Unit и Page Unit ("
               "не уверен), которые обеспечивают работу в соответствующих "
               "режимах адресации памяти. ",
        "GDT": "Global Descriptor Table — глобальная таблица дескрипторов - "
               "служебная структура данных в архитектуре x86, определяющая "
               "глобальные (общие для всех задач) сегменты ",
        "LDT": "Local Descriptor Table — локальная таблица дескрипторов, "
               "доступные для текущей задачи.",
        "GDTR": "Global Descriptor Table Register — регистр глобальной "
                "дескрипторной таблицы, специальный 48-битный регистр, "
                "который описывает местоположение и размер таблицы, "
                "содержащей дескрипторы. ",
        "LDTR": "Local Descriptor Table Register - регистр локальной таблицы "
                "дескрипторов, содержит индекс дескриптора LDT в GDT.",
        "LGBT": "Lesbian Gay Bisexual Transgender (с) wiki",
        "IP": " Instruction Pointer - регистр, хранящий указатель на "
              "следующую инструкцию",
        "SP": "Stack Pointer - указатель на вершину стека",
        "3DNow!": "SIMD-расширение набора инструкций процессора от AMD",
        "CAS": "Column Address Strobe - стробирование столбца, сигнал, "
               "обозначающий, что на шину адреса передается столбец",
        "RAS": "Row Address Strobe - стробирование строки, сигнал, "
               "обозначающий, что на шину адреса передается строка",
        "CS": "Chip Selector - сигнал для выбора банка памяти",
        "Триггер": "класс электронных устройств, обладающих способностью "
                   "длительно находиться в одном из двух устойчивых "
                   "состояний и чередовать их под воздействием внешних "
                   "сигналов. ",
        "Big Endian": "задает порядок байт слева направо",
        "Little Endian": "справа налево",
        "CISC": "Complex Instruction Set Computer — компьютер с полным "
                "набором команд",
        "RISC": "Reduced Instruction Set Computer — компьютер с сокращенным "
                "набором команд",
        "VLIW": "Very Long Instruction Word",
        "EPIC": "Explicity Parallel Instruction Computing",
        "LRU": "Least Recenly Used - алгоритм удаления наиболее давно "
               "использовавшихся элементов (в кеш памяти)",
        "FIFO": "First-in First-out — первым поступил, первым выводится. FIFO "
                "удаляет  ту страницу, которая раньше всех загружалась, "
                "независимо от того, когда в  последний раз производилось "
                "обращение к этой странице",
        "MS": "модельно-специфицированные данные, типы данных, специфичные "
              "для определенной архитектуры.",
        "MSR": "модельно-специфицированные регистры (прим.: MMX[0-7], "
               "XMM[0-7])",
        "Кэш": "сверхбыстрая память, основанная на триггерах",
        "PE": "Portable Executable - формат исполняемых файлов (Шиндовс)",
        "SRAM": "Static RAM (см. RAM) - Статическая память произвольного "
                "доступа (используются триггеры для хранения информации)",
        "FPM RAM": "Fast Page Mode RAM - RAM с быстрым страничным доступом, "
                   "в которой при повторном запросе ячейки из той же строки "
                   "не требуется подача сигнала RAS#",
        "EDO RAM": "Extend Data Out RAM - сигнал CAS# сбрасывается до "
                   "окончания передачи данных, тем самым память готова к "
                   "следующему запросу.",
        "BEDO": "Burst EDO RAM - разработчики добавили счетчик столбцов, "
                "что позволило выводить на шину данных до четырех смежных "
                "ячеек памяти.",
        "SDRAM": "Synchronous DRAM - работает синхронно с контролером, "
                 "усовершенствован пакетный режим (снято ограничение в 4 "
                 "ячейки, т.к. используется полноразрядный счетчие)",
        "DDR SDRAM": "Double Data Rate - SDRAM с удвоенной скоростью передачи "
                     "данных. Данные в DDR SDRAM передаются и по фронту, "
                     "и по спаду тактового импульса.",
        "Шина": "это группа проводников, соединяющих различные устройства. "
                "Шины можно разделить на группы в соответствии с "
                "выполняемыми функциями. Они могут быть внутренними по "
                "отношению к процессору и служить для передачи данных в АЛУ "
                "и из АЛУ, а могут быть внешними по отношению к процессору и "
                "связывать процессор с памятью или устройствами "
                "ввода-вывода. ",
        "Cлово": "совокупность смежных байт памяти фиксированной длины, "
                 "зависящее от аппаратной платформы и программного "
                 "обеспечения. Под машинным словом понимается минимальная "
                 "единица обмена между процессором и памятью. Размер "
                 "определяется разрядностью шины и разрядностью регистров "
                 "процессора. Биты в слове нумеруются с 0. В Little Endian — "
                 "байты внутри машинного слова нумеруются справа налево("
                 "x86). В Big Endian — байты внутри машинного слова "
                 "нумеруются слева направо(ARM). ",
        "Память": "часть вычислительной машины, физическое устройство или "
                  "среда для хранения данных, используемая в вычислениях.",
        "Двойное слово": "машинное слово двойной длины",
        "Бит": "основная единица памяти. Бит может содержать 0 или 1. Это "
               "самая маленькая единица памяти",
        "Байт": "минимальная адресуемая единица памяти",
        "Вентиль": "цифровая схема, реализующая определённую базовую "
                   "логическую операцию",
}

tickets = ["Устройство простейшего компьютера и адресация",
           "Принципы фон Неймана",
           "УУ и АЛУ. Типы команд. Измерение производительности компьютера",
           "Системы счисления. Двоичная, восьмеричная и шестнадцатеричная "
           "арифметика",
           "Цифровая логика и операции над битами",
           "Простейшие способы оптимизации выполнениякоманд. CISC и RISC. "
           "Принципы RISC",
           "Методы работы с внешними устройствами.  Типы прерываний и "
           "структура обработчика",
           "Представление данных в ЭВМ. Форматы данных. Представление целых "
           "чисел",
           "Представление данных в ЭВМ. Форматы  данных. Представление чисел "
           "с плавающей точкой",
           "Представление данных в ЭВМ. Форматы данных. Символьные данные. "
           "Массивы. Строки.Стек",
           "Представление данных в ЭВМ. Форматы данных. BCD. Структуры. "
           "Специальные типыданных",
           "Методы адресации и использование регистров при адресации. "
           "Непосредственная, прямая, регистровая и косвенная регистровая "
           "адресация",
           "Методы адресации и использование регистров  при   адресации.   "
           "Индексная   и   относительная  индексная адресация. "
           "Использование стека приадресации",
           "Методы адресации и использование регистровпри адресации. "
           "Представление адреса в командах перехода. Представление адреса "
           "сиспользованием сегментных регистров",
           "Три основные архитектуры организации кэша",
           "Кэш. Типы кэш-памяти по стратегии обновления  основной памяти. "
           "Механизмы замещения строк.  Организация кэш-памяти в "
           "современных ЭВМ",
           "Архитектура с общей шиной.Децентрализованный арбитраж",
           "Архитектура с общей шиной. Централизованныйарбитраж. Структура "
           "приоритетов прицентрализованном арбитраже",
           "Архитектура с общей шиной. Механизмыобмена данными",
           "Организация конвейера команд. Скалярный,суперскалярный и "
           "суперконвейерныйвычислитель",
           "Основы схемотехники, базовые элементы,конструирование булевых "
           "функций",
           "Предсказание переходов. Регистровые окна ипереименование "
           "регистров",
           "Классификация Флинна с примерамиреализации архитектур",
           "Архитектуры VLIW и EPIC. Особенности  спекулятивного исполнения "
           "инструкций вархитектуре EPIC",
           "Закон Амдала",
           "Дополнения Ванга и Бриггса к классификации Флинна",
           "Архитектура MIPS",
           "Согласование кэшей в мультипроцессорныхсистемах и многоядерных "
           "процессорах",
           "Архитектура SPARC",
           "Характеристики машинных команд",
           "Архитектура системы команд. Три основныеклассификации, примеры",
           "Сегментная модель памяти. Страничная модельпамяти",
           "Режимы работы процессоров INTEL х86.  Уровни привилегий в "
           "защищенном режиме",
           "Работа процессоров INTEL х86 в защищенномрежиме",
           "Физическая организация DRAM",
           "DRAMТипы DRAM, схемы пакетных циклов"
           ]

app.config['NAMES'] = tickets
app.config['DICTIONARY'] = dictionary_words
