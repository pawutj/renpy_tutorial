label ch1:
    play music "audio/bgm/wakuwaku.mp3"
    scene park with dissolve
    
    show ayase normal
    ayase normal "คะแนนของพวกเธอสองคนเข้าขั้นวิกฤตแล้ว" with dissolve
    ayase angry "พวกเธอสองคนรู้ตัวรึเปล่า" with dissolve
    hide ayase 

    show eri normal at left
    show mikan normal at right
    mikan smile "ฉันขาดอีกสามคะแนนก็ผ่านแล้ว" with dissolve
    eri angry "สามคะแนนที่ไหน สามสิบ ต่างหาก!" with dissolve
    mikan normal "เอ๋ ~" with dissolve
    hide eri
    hide mikan

    show ayase normal
    ayase normal "ไม่ต้องมาเอ๋เลย ฉันจะติวให้พวกเธอเอง" with dissolve
    ayase smile "เริ่มจากวิชาเคมีก่อน" with dissolve
    hide ayase 

    menu :
        "เคมีที่เป็นสาขาที่ว่าด้วยการเปลี่ยนสภาพของสสาร?":
            show eri angry
            eri smile "วันนี้เธอจริงจังแปลกๆนะเนี่ย" with dissolve
            $ ans = True
            hide eri
        "เคมีที่มันอยู่ในวัด?":
            show eri angry
            eri angry "นั่นมันเจดีห์" with dissolve
            $ ans = False
            hide eri
        "เคมีที่เป็นคู่แข่งมาเวล?":
            show eri angry
            eri angry "นั่นมัน DC" with dissolve
            $ ans = False
            hide eri

    if ans == True :
        show ayase normal
        ayase normal "ตั้งใจติวแบบนี้ เกรด A น่าจะแค่เอื้อมแล้ว" with dissolve
        hide ayase
    else:
        show ayase angry
        ayase angry "ถ้าพวกเธอเล่นกันแบบนี้ พวกเธอจะเอาอะไรไปสอบ" with dissolve
        hide ayase

        show mikan smile
        mikan smile "อะไรที่เป็นบริษัทขายของเล่น?" with dissolve
        hide mikan

        show ladder
        ayase angry "แล้วนี่ ใช่บันไดรึเปล่า" with dissolve
        play sound "audio/sfx/tukkomi.mp3"
        hide ayase

    scene black with Dissolve(2.0)

    return

