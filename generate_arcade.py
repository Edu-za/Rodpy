#!/usr/bin/env python3
"""Generate Rodpy / PyPals math + coding game pack (static HTML)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent

FONT_LINKS = """  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;800&family=Space+Grotesk:wght@400;600;700&family=IBM+Plex+Mono:wght@500&display=swap" rel="stylesheet" />"""

BASE_CSS = r"""
:root{
  --ink:#12231c;--leaf:#1f7a4c;--leaf-deep:#0f4d32;--sun:#f4b942;--coral:#e76f51;
  --p1:#1f7a4c;--p2:#c45c26;--cream:#f3faf5;--panel:#fff;--code:#143528;
  --shadow:0 14px 32px rgba(15,77,50,.14);
}
*{box-sizing:border-box}body{margin:0;font-family:"Space Grotesk",system-ui,sans-serif;color:var(--ink);
background:radial-gradient(900px 480px at 0% 0%,#b8f0c8 0%,transparent 55%),
radial-gradient(800px 420px at 100% 0%,#ffe0c2 0%,transparent 50%),
linear-gradient(180deg,#eaf8ef,#f3faf5);min-height:100vh;line-height:1.45}
.wrap{width:min(1060px,calc(100% - 1.4rem));margin:0 auto;padding:1rem 0 2rem}
.brand{font-family:"Baloo 2",cursive;font-weight:800;font-size:1.35rem;text-decoration:none;color:var(--ink)}
.brand span{color:var(--sun)}.hidden{display:none!important}
.btn{border:0;font:inherit;font-weight:700;cursor:pointer;border-radius:999px;padding:.75rem 1.2rem;transition:transform .15s}
.btn:hover{transform:translateY(-2px)}.btn-sun{background:var(--sun);color:var(--ink);box-shadow:0 8px 18px rgba(244,185,66,.35)}
.btn-p1{background:var(--p1);color:#fff}.btn-p2{background:var(--p2);color:#fff}.btn-ghost{background:#fff;border:2px solid rgba(18,35,28,.1)}
input[type=text],input[type=number]{width:100%;font:inherit;padding:.65rem .8rem;border-radius:12px;border:2px solid #cfe3d7;background:#f7fcf9}
input:focus{outline:none;border-color:var(--leaf);box-shadow:0 0 0 3px rgba(31,122,76,.15)}
.card{background:var(--panel);border-radius:20px;padding:1.1rem 1.15rem;box-shadow:var(--shadow);margin-bottom:1rem}
h1,h2{font-family:"Baloo 2",cursive;line-height:1.05;margin:0 0 .4rem}
.muted{color:rgba(18,35,28,.7)}.mono{font-family:"IBM Plex Mono",monospace}
.hud{display:flex;flex-wrap:wrap;gap:.6rem;align-items:center;justify-content:space-between;margin:.4rem 0 1rem}
.pill{display:flex;gap:.45rem;align-items:center;background:#fff;padding:.4rem .8rem;border-radius:999px;box-shadow:var(--shadow);font-weight:700}
.pill .dot{width:10px;height:10px;border-radius:50%}.pill.p1 .dot{background:var(--p1)}.pill.p2 .dot{background:var(--p2)}
.track{background:var(--code);border-radius:18px;padding:.9rem;margin-bottom:1rem;color:#c8ebd8}
.lane{position:relative;height:48px;margin:.45rem 0;border-radius:12px;background:repeating-linear-gradient(90deg,rgba(255,255,255,.06) 0 28px,rgba(255,255,255,.02) 28px 56px);border:1px solid rgba(255,255,255,.08)}
.finish{position:absolute;right:10px;top:6px;bottom:6px;width:10px;background:repeating-linear-gradient(#fff 0 4px,#12231c 4px 8px);opacity:.85}
.racer{position:absolute;left:8px;top:50%;transform:translateY(-50%);font-size:1.7rem;transition:left .5s cubic-bezier(.22,1,.36,1)}
.arena{display:grid;grid-template-columns:1fr 1fr;gap:.8rem}@media(max-width:700px){.arena{grid-template-columns:1fr}}
.pad{border:3px solid;border-radius:16px;padding:.85rem;background:#f7fcf9}.pad.p1{border-color:var(--p1)}.pad.p2{border-color:var(--p2)}
.pad.locked{opacity:.55;pointer-events:none}.pad.winner{background:#fff8e6}
.fb{min-height:1.2rem;font-weight:700;font-size:.9rem;margin-top:.4rem}.fb.ok{color:var(--leaf-deep)}.fb.no{color:#b42318}
.banner{text-align:center;font-family:"Baloo 2",cursive;font-size:1.25rem;min-height:1.5rem;margin:.7rem 0 0}
.prompt{font-size:clamp(1.4rem,4vw,2rem);font-family:"Baloo 2",cursive;text-align:center;margin:.6rem 0}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:.8rem}@media(max-width:700px){.grid2{grid-template-columns:1fr}}
.choice{border:2px solid #cfe3d7;background:#fff;border-radius:14px;padding:.85rem;cursor:pointer;font-weight:700;text-align:center}
.choice:hover{border-color:var(--leaf);background:#f0faf4}.choice.good{border-color:var(--leaf);background:#d8f3e4}.choice.bad{border-color:#b42318;background:#fdecea}
.board{display:grid;gap:.55rem}.stars{display:flex;gap:.35rem;margin:.5rem 0}.star{width:26px;height:26px;border-radius:50%;background:#d7e8de}.star.on{background:var(--sun)}
footer{text-align:center;color:rgba(18,35,28,.5);font-size:.85rem;padding:0 0 1.5rem}
.confetti{pointer-events:none;position:fixed;inset:0;overflow:hidden;z-index:40}.confetti i{position:absolute;top:-12px;width:10px;height:14px;border-radius:2px;animation:fall linear forwards}
@keyframes fall{to{transform:translateY(110vh) rotate(520deg)}}
"""


def page(title: str, body: str, extra_js: str = "") -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
{FONT_LINKS}
  <style>{BASE_CSS}</style>
</head>
<body>
{body}
<footer><a class="brand" href="index.html">Rodpy Arcade</a> · open in your browser</footer>
<script>
function confettiBurst(){{
  let box=document.getElementById('confetti');
  if(!box){{box=document.createElement('div');box.id='confetti';box.className='confetti';document.body.appendChild(box);}}
  box.classList.remove('hidden');box.innerHTML='';
  const colors=['#f4b942','#1f7a4c','#e76f51','#2a9d8f','#fff'];
  for(let i=0;i<40;i++){{const b=document.createElement('i');b.style.left=Math.random()*100+'%';b.style.background=colors[i%colors.length];b.style.animationDuration=(1.1+Math.random()*1.3)+'s';box.appendChild(b);}}
  setTimeout(()=>box.classList.add('hidden'),2600);
}}
{extra_js}
</script>
</body>
</html>
"""


def race_game(
    filename: str,
    title: str,
    tagline: str,
    emoji1: str,
    emoji2: str,
    win_score: int,
    gen_js: str,
) -> None:
    body = f"""
<div id="lobby" class="wrap">
  <a class="brand" href="index.html">Rodpy ←</a>
  <div class="card" style="margin-top:1rem;background:linear-gradient(135deg,#1f7a4c,#c45c26);color:#fff">
    <h1>{title}</h1>
    <p style="margin:0;opacity:.95">{tagline}</p>
  </div>
  <div class="grid2">
    <div class="card"><h2 style="color:var(--p1)">Player 1</h2><label>Name</label><input id="n1" value="Ada" maxlength="12"/></div>
    <div class="card"><h2 style="color:var(--p2)">Player 2</h2><label>Name</label><input id="n2" value="Byte" maxlength="12"/></div>
  </div>
  <button class="btn btn-sun" id="start" style="width:100%">Start duel →</button>
</div>
<div id="game" class="wrap hidden">
  <div class="hud">
    <a class="brand" href="index.html">Rodpy</a>
    <div class="pill" id="roundPill">Round</div>
    <div style="display:flex;gap:.5rem;flex-wrap:wrap">
      <div class="pill p1"><span class="dot"></span><span id="l1">Ada</span> <strong id="s1">0</strong></div>
      <div class="pill p2"><span class="dot"></span><span id="l2">Byte</span> <strong id="s2">0</strong></div>
    </div>
  </div>
  <div class="track">
    <div style="font-size:.8rem;letter-spacing:.06em;text-transform:uppercase;margin-bottom:.4rem">First to {win_score} wins</div>
    <div class="lane"><span class="racer" id="r1">{emoji1}</span><div class="finish"></div></div>
    <div class="lane"><span class="racer" id="r2">{emoji2}</span><div class="finish"></div></div>
  </div>
  <div class="card">
    <div class="prompt" id="q">?</div>
    <p class="muted" id="hint" style="text-align:center;margin:0 0 .8rem"></p>
    <div class="arena">
      <div class="pad p1" id="pad1"><h2 id="t1" style="color:var(--p1);font-size:1.15rem">Ada</h2>
        <input id="a1" autocomplete="off"/><button class="btn btn-p1" style="width:100%;margin-top:.5rem" data-p="1">Submit</button>
        <div class="fb" id="f1"></div></div>
      <div class="pad p2" id="pad2"><h2 id="t2" style="color:var(--p2);font-size:1.15rem">Byte</h2>
        <input id="a2" autocomplete="off"/><button class="btn btn-p2" style="width:100%;margin-top:.5rem" data-p="2">Submit</button>
        <div class="fb" id="f2"></div></div>
    </div>
    <div class="banner" id="banner">Ready…</div>
  </div>
  <button class="btn btn-ghost" id="quit">Lobby</button>
</div>
<div id="win" class="wrap hidden">
  <div class="card" style="text-align:center;padding:2rem">
    <div style="font-size:3.5rem">🏆</div>
    <h1 id="wtitle">Winner</h1>
    <p id="wsub" class="muted"></p>
    <p><span id="fn1"></span>: <strong id="fs1"></strong> · <span id="fn2"></span>: <strong id="fs2"></strong></p>
    <button class="btn btn-sun" id="again">Play again</button>
  </div>
</div>
"""
    js = f"""
const WIN={win_score};
let names=['Ada','Byte'], scores=[0,0], locked=false, cur=null;
const $=(id)=>document.getElementById(id);
function show(id){{['lobby','game','win'].forEach(s=>$(s).classList.toggle('hidden',s!==id));}}
function track(){{
  [0,1].forEach(i=>{{const pct=Math.min(82,(scores[i]/WIN)*82);$('r'+(i+1)).style.left='calc(8px + '+pct+'% )';}});
}}
function upd(){{$('s1').textContent=scores[0];$('s2').textContent=scores[1];track();}}
{gen_js}
function loadQ(){{
  locked=false;cur=nextQuestion();
  $('q').textContent=cur.prompt;$('hint').textContent=cur.hint||'';
  $('a1').value='';$('a2').value='';$('f1').textContent='';$('f2').textContent='';
  $('f1').className='fb';$('f2').className='fb';
  $('pad1').classList.remove('locked','winner');$('pad2').classList.remove('locked','winner');
  $('banner').textContent='First correct wins the round!';$('a1').focus();
}}
function submit(p){{
  if(locked||!cur)return;
  const v=$('a'+p).value; const ok=cur.check(v);
  const f=$('f'+p);
  if(!ok){{f.className='fb no';f.textContent='Nope — try again!';return;}}
  locked=true;scores[p-1]++;f.className='fb ok';f.textContent='+1!';
  $('pad'+p).classList.add('winner');$('pad'+(p===1?2:1)).classList.add('locked');
  $('banner').textContent=names[p-1]+' wins the round!';upd();
  if(scores[0]>=WIN||scores[1]>=WIN){{setTimeout(endGame,700);}} else {{setTimeout(loadQ,850);}}
}}
function endGame(){{
  const a=scores[0],b=scores[1];
  let t,s; if(a>b){{t=names[0]+' wins!';s='Green lane takes it.';}} else if(b>a){{t=names[1]+' wins!';s='Orange lane takes it.';}} else {{t=\"It's a tie!\";s='Both crushed it.';}}
  $('wtitle').textContent=t;$('wsub').textContent=s;
  $('fn1').textContent=names[0];$('fn2').textContent=names[1];$('fs1').textContent=a;$('fs2').textContent=b;
  confettiBurst();show('win');
}}
$('start').onclick=()=>{{
  names=[($('n1').value.trim()||'Player 1').slice(0,12),($('n2').value.trim()||'Player 2').slice(0,12)];
  scores=[0,0];$('l1').textContent=names[0];$('l2').textContent=names[1];$('t1').textContent=names[0];$('t2').textContent=names[1];
  upd();show('game');loadQ();
}};
$('again').onclick=()=>show('lobby');$('quit').onclick=()=>show('lobby');
document.querySelectorAll('button[data-p]').forEach(b=>b.onclick=()=>submit(+b.dataset.p));
$('a1').onkeydown=e=>{{if(e.key==='Enter')submit(1);}};
$('a2').onkeydown=e=>{{if(e.key==='Enter')submit(2);}};
"""
    (ROOT / filename).write_text(page(title + " · Rodpy", body, js), encoding="utf-8")
    print("wrote", filename)


def write_hub() -> None:
    """Hub is the GitHub-style index.html (hand-maintained). Do not overwrite it."""
    print("skip index.html (GitHub-style hub is hand-maintained)")
    return


def write_solo_pages() -> None:
    # Number bonds
    (ROOT / "bonds.html").write_text(
        page(
            "Number Bond Builder · Rodpy",
            """
<div class="wrap">
  <a class="brand" href="index.html">Rodpy ←</a>
  <div class="card" style="margin-top:1rem"><h1>Number Bond Builder</h1>
  <p class="muted">Find the missing partner. Make the target number.</p>
  <div class="stars" id="stars"></div>
  <div class="prompt" id="q">7 + ? = 10</div>
  <input id="ans" type="number" placeholder="?" />
  <button class="btn btn-sun" id="go" style="width:100%;margin-top:.7rem">Check</button>
  <div class="fb" id="fb"></div>
  <p class="muted" id="score">Score: 0</p>
  </div>
</div>""",
            """
let score=0, target=10, shown=0, miss=0;
const $=id=>document.getElementById(id);
function mk(){target=Math.random()<.5?10:100; shown=target===10?1+Math.floor(Math.random()*9):10+Math.floor(Math.random()*80); miss=target-shown;
  $('q').textContent=shown+' + ? = '+target; $('ans').value=''; $('fb').textContent=''; $('ans').focus();}
function stars(){const s=$('stars');s.innerHTML='';for(let i=0;i<5;i++){const d=document.createElement('div');d.className='star'+(i<Math.min(5,Math.floor(score/2))?' on':'');s.appendChild(d);}}
$('go').onclick=()=>{if(Number($('ans').value)===miss){score++;$('fb').className='fb ok';$('fb').textContent='Yes!';if(score%5===0)confettiBurst();stars();$('score').textContent='Score: '+score;setTimeout(mk,500);}
else{$('fb').className='fb no';$('fb').textContent='Try again — partner is not that.';}};
$('ans').onkeydown=e=>{if(e.key==='Enter')$('go').click();}; mk(); stars();
""",
        ),
        encoding="utf-8",
    )

    (ROOT / "shapes.html").write_text(
        page(
            "Shape Sorter · Rodpy",
            """
<div class="wrap">
  <a class="brand" href="index.html">Rodpy ←</a>
  <div class="card" style="margin-top:1rem"><h1>Shape Sorter</h1>
  <p class="muted">Tap the bin that matches the shape.</p>
  <div class="prompt" id="shape" style="font-size:4rem">🔺</div>
  <p style="text-align:center;font-weight:700" id="name">Triangle</p>
  <div class="board" style="grid-template-columns:repeat(3,1fr);display:grid;gap:.55rem;margin-top:1rem" id="bins"></div>
  <div class="fb" id="fb" style="text-align:center"></div>
  <p class="muted" id="score">Score: 0</p>
  </div>
</div>""",
            """
const shapes=[{e:'🔺',n:'Triangle',b:'3 sides'},{e:'⬛',n:'Square',b:'4 equal sides'},{e:'🔵',n:'Circle',b:'Round'},{e:'▰',n:'Parallelogram',b:'4 sides slanted'},{e:'⬟',n:'Pentagon',b:'5 sides'},{e:'⬡',n:'Hexagon',b:'6 sides'}];
const bins=['3 sides','4 equal sides','Round','4 sides slanted','5 sides','6 sides'];
let cur=null,score=0; const $=id=>document.getElementById(id);
function deal(){cur=shapes[Math.floor(Math.random()*shapes.length)];$('shape').textContent=cur.e;$('name').textContent=cur.n;$('fb').textContent='';
  const box=$('bins');box.innerHTML='';bins.forEach(b=>{const c=document.createElement('button');c.className='choice';c.textContent=b;c.onclick=()=>pick(b);box.appendChild(c);});}
function pick(b){if(b===cur.b){score++;$('fb').className='fb ok';$('fb').textContent='Sorted!';$('score').textContent='Score: '+score;if(score%5===0)confettiBurst();setTimeout(deal,450);}
else{$('fb').className='fb no';$('fb').textContent='Not that bin.';}} deal();
""",
        ),
        encoding="utf-8",
    )

    (ROOT / "angles.html").write_text(
        page(
            "Angle Archer · Rodpy",
            """
<div class="wrap">
  <a class="brand" href="index.html">Rodpy ←</a>
  <div class="card" style="margin-top:1rem"><h1>Angle Archer</h1>
  <p class="muted">What type of angle is shown? (closest guess wins points)</p>
  <svg id="svg" viewBox="0 0 200 140" width="100%" style="background:#143528;border-radius:14px;max-height:220px"></svg>
  <p class="prompt" id="deg">?°</p>
  <div class="grid2" id="opts"></div>
  <div class="fb" id="fb" style="text-align:center"></div>
  <p class="muted" id="score">Score: 0</p>
  </div>
</div>""",
            """
let angle=0,score=0; const $=id=>document.getElementById(id);
function typeOf(a){if(a===90)return 'Right';if(a===180)return 'Straight';if(a<90)return 'Acute';if(a<180)return 'Obtuse';return 'Reflex';}
function draw(a){const svg=$('svg'); const rad=a*Math.PI/180; const x=100+70*Math.cos(-rad), y=100+70*Math.sin(-rad);
  svg.innerHTML=`<line x1="100" y1="100" x2="170" y2="100" stroke="#f4b942" stroke-width="4"/>
  <line x1="100" y1="100" x2="${x}" y2="${y}" stroke="#7dd3a7" stroke-width="4"/>
  <circle cx="100" cy="100" r="4" fill="#fff"/>`;
  $('deg').textContent=a+'°';}
function deal(){angle=[30,45,60,90,120,135,150,180][Math.floor(Math.random()*8)];draw(angle);$('fb').textContent='';
  const opts=['Acute','Right','Obtuse','Straight']; const box=$('opts');box.innerHTML='';
  opts.forEach(o=>{const b=document.createElement('button');b.className='choice';b.textContent=o;b.onclick=()=>pick(o);box.appendChild(b);});}
function pick(o){if(o===typeOf(angle)){score++;$('fb').className='fb ok';$('fb').textContent='Bullseye!';$('score').textContent='Score: '+score;if(score%4===0)confettiBurst();setTimeout(deal,500);}
else{$('fb').className='fb no';$('fb').textContent='Hint: acute<90, right=90, obtuse>90, straight=180';}} deal();
""",
        ),
        encoding="utf-8",
    )

    (ROOT / "coordinates.html").write_text(
        page(
            "Coordinate Quest · Rodpy",
            """
<div class="wrap">
  <a class="brand" href="index.html">Rodpy ←</a>
  <div class="card" style="margin-top:1rem"><h1>Coordinate Quest</h1>
  <p class="muted">Read the point on the grid. Type x,y</p>
  <svg id="grid" viewBox="0 0 220 220" width="100%" style="background:#fff;border-radius:14px;border:2px solid #cfe3d7;max-width:320px;display:block;margin:0 auto"></svg>
  <p class="prompt">Point = (?, ?)</p>
  <input id="ans" placeholder="e.g. 3,2" class="mono"/>
  <button class="btn btn-sun" id="go" style="width:100%;margin-top:.7rem">Check</button>
  <div class="fb" id="fb"></div>
  <p class="muted" id="score">Score: 0</p>
  </div>
</div>""",
            """
let x=0,y=0,score=0; const $=id=>document.getElementById(id);
function draw(){x=1+Math.floor(Math.random()*5);y=1+Math.floor(Math.random()*5);
  const g=$('grid'); let h='';
  for(let i=0;i<=6;i++){const p=20+i*30;h+=`<line x1="${p}" y1="20" x2="${p}" y2="200" stroke="#d7e8de"/><line x1="20" y1="${p}" x2="200" y2="${p}" stroke="#d7e8de"/>`;}
  h+=`<line x1="20" y1="200" x2="200" y2="200" stroke="#12231c" stroke-width="2"/><line x1="20" y1="20" x2="20" y2="200" stroke="#12231c" stroke-width="2"/>`;
  const px=20+x*30, py=200-y*30; h+=`<circle cx="${px}" cy="${py}" r="7" fill="#e76f51"/>`;
  g.innerHTML=h;$('ans').value='';$('fb').textContent='';}
$('go').onclick=()=>{const m=$('ans').value.trim().match(/^(-?\\d+)\\s*,\\s*(-?\\d+)$/);
  if(m&&+m[1]===x&&+m[2]===y){score++;$('fb').className='fb ok';$('fb').textContent='Mapped!';$('score').textContent='Score: '+score;if(score%5===0)confettiBurst();setTimeout(draw,450);}
  else{$('fb').className='fb no';$('fb').textContent='Format: x,y — count from origin (bottom-left).';}};
$('ans').onkeydown=e=>{if(e.key==='Enter')$('go').click();}; draw();
""",
        ),
        encoding="utf-8",
    )

    (ROOT / "patterns.html").write_text(
        page(
            "Pattern Prophet · Rodpy",
            """
<div class="wrap">
  <a class="brand" href="index.html">Rodpy ←</a>
  <div class="card" style="margin-top:1rem"><h1>Pattern Prophet</h1>
  <p class="muted">What comes next in the sequence?</p>
  <div class="prompt mono" id="q">2, 4, 6, 8, ?</div>
  <input id="ans" type="number"/>
  <button class="btn btn-sun" id="go" style="width:100%;margin-top:.7rem">Check</button>
  <div class="fb" id="fb"></div>
  <p class="muted" id="score">Score: 0</p>
  </div>
</div>""",
            """
let next=0,score=0; const $=id=>document.getElementById(id);
function deal(){const kind=Math.random(); let seq=[],n;
  if(kind<.4){const a=1+Math.floor(Math.random()*5),d=1+Math.floor(Math.random()*4);seq=[a,a+d,a+2*d,a+3*d];n=a+4*d;}
  else if(kind<.75){let a=1+Math.floor(Math.random()*3),r=2;seq=[a,a*r,a*r*r,a*r*r*r];n=a*r*r*r*r;}
  else {const a=2+Math.floor(Math.random()*4);seq=[a,a+1,a+3,a+6];n=a+10;} // +1,+2,+3
  next=n;$('q').textContent=seq.join(', ')+', ?';$('ans').value='';$('fb').textContent='';}
$('go').onclick=()=>{if(Number($('ans').value)===next){score++;$('fb').className='fb ok';$('fb').textContent='Prophecy correct!';$('score').textContent='Score: '+score;if(score%5===0)confettiBurst();setTimeout(deal,500);}
else{$('fb').className='fb no';$('fb').textContent='Look for +d or ×r patterns.';}};
$('ans').onkeydown=e=>{if(e.key==='Enter')$('go').click();}; deal();
""",
        ),
        encoding="utf-8",
    )

    (ROOT / "market.html").write_text(
        page(
            "Market Math · Rodpy",
            """
<div class="wrap">
  <a class="brand" href="index.html">Rodpy ←</a>
  <div class="card" style="margin-top:1rem"><h1>Market Math (ZMW)</h1>
  <p class="muted">You are at a market stall. Work out the change.</p>
  <div class="prompt" id="q" style="font-size:1.35rem;line-height:1.25">?</div>
  <input id="ans" type="number" placeholder="Change in ZMW"/>
  <button class="btn btn-sun" id="go" style="width:100%;margin-top:.7rem">Pay</button>
  <div class="fb" id="fb"></div>
  <p class="muted" id="score">Score: 0</p>
  </div>
</div>""",
            """
const items=[['tomato box',15],['chitenge',80],['loaf',12],['airtime',20],['mangoes',25],['fish',45]];
let change=0,score=0; const $=id=>document.getElementById(id);
function deal(){const [name,price]=items[Math.floor(Math.random()*items.length)];
  const pay=[20,50,100,200].filter(p=>p>=price)[Math.floor(Math.random()*3)]||100;
  change=pay-price; $('q').textContent=`${name} costs K${price}. You pay K${pay}. Change?`; $('ans').value='';$('fb').textContent='';}
$('go').onclick=()=>{if(Number($('ans').value)===change){score++;$('fb').className='fb ok';$('fb').textContent='Correct change!';$('score').textContent='Score: '+score;if(score%5===0)confettiBurst();setTimeout(deal,500);}
else{$('fb').className='fb no';$('fb').textContent='Change = money given − price';}};
$('ans').onkeydown=e=>{if(e.key==='Enter')$('go').click();}; deal();
""",
        ),
        encoding="utf-8",
    )

    (ROOT / "travel.html").write_text(
        page(
            "Travel Graph Dash · Rodpy",
            """
<div class="wrap">
  <a class="brand" href="index.html">Rodpy ←</a>
  <div class="card" style="margin-top:1rem"><h1>Travel Graph Dash</h1>
  <p class="muted">A bus moves. Read the story from the numbers.</p>
  <div class="prompt" id="q" style="font-size:1.25rem;line-height:1.3">?</div>
  <input id="ans" type="number"/>
  <button class="btn btn-sun" id="go" style="width:100%;margin-top:.7rem">Check</button>
  <div class="fb" id="fb"></div>
  <p class="muted" id="score">Score: 0</p>
  </div>
</div>""",
            """
let ans=0,score=0; const $=id=>document.getElementById(id);
function deal(){const t=1+Math.floor(Math.random()*4), kind=Math.random();
  if(kind<.5){const s=20+Math.floor(Math.random()*20); const d=s*t; ans=s; $('q').textContent=`A bus travels ${d} km in ${t} hours at steady speed. Speed (km/h)?`;}
  else {const s=20+Math.floor(Math.random()*40); ans=s*t; $('q').textContent=`Speed ${s} km/h for ${t} hours. Distance (km)?`;}
  $('ans').value='';$('fb').textContent='';}
$('go').onclick=()=>{if(Number($('ans').value)===ans){score++;$('fb').className='fb ok';$('fb').textContent='Graph sense!';$('score').textContent='Score: '+score;if(score%5===0)confettiBurst();setTimeout(deal,500);}
else{$('fb').className='fb no';$('fb').textContent='Remember: speed = distance ÷ time';}};
$('ans').onkeydown=e=>{if(e.key==='Enter')$('go').click();}; deal();
""",
        ),
        encoding="utf-8",
    )

    (ROOT / "earth.html").write_text(
        page(
            "Earth Geometry · Rodpy",
            """
<div class="wrap">
  <a class="brand" href="index.html">Rodpy ←</a>
  <div class="card" style="margin-top:1rem"><h1>Earth Geometry Lite</h1>
  <p class="muted">Latitude & longitude basics for explorers.</p>
  <div class="prompt" id="q" style="font-size:1.2rem;line-height:1.35">?</div>
  <div class="grid2" id="opts"></div>
  <div class="fb" id="fb" style="text-align:center"></div>
  <p class="muted" id="score">Score: 0</p>
  </div>
</div>""",
            """
const qs=[
 {q:'Lines that run east–west and measure north/south are called…', a:'Latitude', opts:['Latitude','Longitude','Altitude','Meridians']},
 {q:'The equator has latitude…', a:'0°', opts:['0°','90°','180°','45°']},
 {q:'Lusaka is in the Southern Hemisphere, so its latitude is…', a:'South', opts:['North','South','East','West']},
 {q:'A full circle around Earth is…', a:'360°', opts:['90°','180°','360°','100°']},
 {q:'Longitude lines meet at the…', a:'Poles', opts:['Equator','Poles','Tropics','Ocean']},
];
let cur=null,score=0; const $=id=>document.getElementById(id);
function deal(){cur=qs[Math.floor(Math.random()*qs.length)];$('q').textContent=cur.q;$('fb').textContent='';
  const box=$('opts');box.innerHTML='';cur.opts.forEach(o=>{const b=document.createElement('button');b.className='choice';b.textContent=o;b.onclick=()=>pick(o);box.appendChild(b);});}
function pick(o){if(o===cur.a){score++;$('fb').className='fb ok';$('fb').textContent='Explorer rank up!';$('score').textContent='Score: '+score;if(score%4===0)confettiBurst();setTimeout(deal,500);}
else{$('fb').className='fb no';$('fb').textContent='Not quite — think equator & poles.';}} deal();
""",
        ),
        encoding="utf-8",
    )

    (ROOT / "lp.html").write_text(
        page(
            "LP Region Rush · Rodpy",
            """
<div class="wrap">
  <a class="brand" href="index.html">Rodpy ←</a>
  <div class="card" style="margin-top:1rem"><h1>LP Region Rush</h1>
  <p class="muted">Feasible region lite: which corner is allowed?</p>
  <div class="prompt" id="q" style="font-size:1.15rem;line-height:1.35">?</div>
  <div class="grid2" id="opts"></div>
  <div class="fb" id="fb" style="text-align:center"></div>
  <p class="muted" id="score">Score: 0</p>
  </div>
</div>""",
            """
const qs=[
 {q:'Constraints: x≥0, y≥0, x+y≤4. Is (1,1) feasible?', a:'Yes', opts:['Yes','No']},
 {q:'Constraints: x≥0, y≥0, x+y≤4. Is (5,0) feasible?', a:'No', opts:['Yes','No']},
 {q:'To maximize profit 3x+2y, we evaluate profit at…', a:'Corner points', opts:['Corner points','Any midpoint','Only (0,0)','Infinity']},
 {q:'x≥0 and y≥0 means we stay in…', a:'First quadrant', opts:['First quadrant','Third quadrant','Only x-axis','Outside']},
 {q:'If x+y≤6 and we want more product, the line x+y=6 is the…', a:'Boundary', opts:['Boundary','Origin','Impossible set','Gradient']},
];
let cur=null,score=0; const $=id=>document.getElementById(id);
function deal(){cur=qs[Math.floor(Math.random()*qs.length)];$('q').textContent=cur.q;$('fb').textContent='';
  const box=$('opts');box.innerHTML='';cur.opts.forEach(o=>{const b=document.createElement('button');b.className='choice';b.textContent=o;b.onclick=()=>pick(o);box.appendChild(b);});}
function pick(o){if(o===cur.a){score++;$('fb').className='fb ok';$('fb').textContent='Feasible!';$('score').textContent='Score: '+score;if(score%4===0)confettiBurst();setTimeout(deal,500);}
else{$('fb').className='fb no';$('fb').textContent='Check every inequality carefully.';}} deal();
""",
        ),
        encoding="utf-8",
    )
    print("wrote solo games")


def main() -> None:
    write_hub()
    race_game(
        "tables.html",
        "Times Table Turbo",
        "Two players. Same times-table question. First correct answer moves your racer. First to 5 wins!",
        "⚡",
        "🔥",
        5,
        """
function nextQuestion(){
  const a=2+Math.floor(Math.random()*10), b=2+Math.floor(Math.random()*10), ans=a*b;
  return {prompt:a+' × '+b+' = ?', hint:'Multiplication race', check:v=>Number(String(v).trim())===ans};
}
""",
    )
    race_game(
        "fractions.html",
        "Fraction Frenzy",
        "Simplify the fraction. Type your answer like 1/2. First correct wins the round!",
        "🍕",
        "🧀",
        5,
        """
function gcd(a,b){return b?gcd(b,a%b):a;}
function nextQuestion(){
  const simp=[[1,2],[1,3],[2,3],[1,4],[3,4],[1,5],[2,5],[3,5],[1,6],[5,6],[3,8],[1,8]];
  if(Math.random()<.55){
    const [n,d]=simp[Math.floor(Math.random()*simp.length)];
    const k=2+Math.floor(Math.random()*4); const N=n*k,D=d*k;
    return {prompt:'Simplify '+N+'/'+D, hint:'Divide top and bottom by the same number', check:v=>{
      const m=String(v).trim().match(/^(\\d+)\\s*\\/\\s*(\\d+)$/); if(!m)return false; return +m[1]===n && +m[2]===d;}};
  }
  const pairs=[[1,2,1,3],[2,3,1,2],[3,4,2,3],[1,5,1,4]];
  const [a,b,c,d]=pairs[Math.floor(Math.random()*pairs.length)];
  const left=a/b, right=c/d; const bigger=left>right? (a+'/'+b):(c+'/'+d);
  return {prompt:'Which is larger: '+a+'/'+b+' or '+c+'/'+d+' ?', hint:'Type the larger fraction like 3/4', check:v=>{
    const m=String(v).trim().replace(/\\s/g,''); return m===bigger;}};
}
""",
    )
    race_game(
        "integers.html",
        "Integer Island",
        "Add and subtract integers (negatives allowed). First correct sails forward!",
        "🏝️",
        "⛵",
        5,
        """
function nextQuestion(){
  const a=Math.floor(Math.random()*21)-10, b=Math.floor(Math.random()*21)-10;
  const op=Math.random()<.5?'+':'-'; const ans=op==='+'?a+b:a-b;
  const show=(n)=> (n<0?('('+n+')'):String(n));
  return {prompt:show(a)+' '+op+' '+show(b)+' = ?', hint:'Watch the signs!', check:v=>Number(String(v).trim())===ans};
}
""",
    )
    race_game(
        "percent.html",
        "Percent Sprint",
        "Find the percentage of a number. First correct answer scores!",
        "📈",
        "💨",
        5,
        """
function nextQuestion(){
  const pct=[10,20,25,50,5,75][Math.floor(Math.random()*6)];
  const base=[20,40,80,100,200,60][Math.floor(Math.random()*6)];
  const ans=(pct/100)*base;
  return {prompt:pct+'% of '+base+' = ?', hint:'Percent means per hundred', check:v=>Number(String(v).trim())===ans};
}
""",
    )
    race_game(
        "algebra.html",
        "Algebra Duel",
        "Solve for x. Type the number only. First correct wins the round!",
        "𝑥",
        "𝑦",
        5,
        """
function nextQuestion(){
  const kinds=Math.floor(Math.random()*3);
  if(kinds===0){const x=1+Math.floor(Math.random()*12); const a=1+Math.floor(Math.random()*5); const b=a*x;
    return {prompt:a+'x = '+b+'  →  x = ?', hint:'Divide both sides by '+a, check:v=>Number(String(v).trim())===x};}
  if(kinds===1){const x=1+Math.floor(Math.random()*10); const b=1+Math.floor(Math.random()*8); const sum=x+b;
    return {prompt:'x + '+b+' = '+sum+'  →  x = ?', hint:'Subtract '+b+' from both sides', check:v=>Number(String(v).trim())===x};}
  const x=2+Math.floor(Math.random()*8); const a=2+Math.floor(Math.random()*4); const b=Math.floor(Math.random()*6); const rhs=a*x+b;
  return {prompt:a+'x + '+b+' = '+rhs+'  →  x = ?', hint:'Undo + then ÷', check:v=>Number(String(v).trim())===x};
}
""",
    )
    write_solo_pages()
    # keep existing code-race.html as-is if present; ensure README
    readme = """# Rodpy Arcade

Kid-friendly **math + Python** mini-games (static HTML).

## Open

Open [`index.html`](index.html) in a browser for the full arcade menu.

## Games

### 2-player races
- [PyPals Code Race](code-race.html) — Python `print`, variables, `if`
- [Times Table Turbo](tables.html)
- [Fraction Frenzy](fractions.html)
- [Integer Island](integers.html)
- [Percent Sprint](percent.html)
- [Algebra Duel](algebra.html)

### Solo practice
- [Number Bond Builder](bonds.html)
- [Shape Sorter](shapes.html)
- [Angle Archer](angles.html)
- [Coordinate Quest](coordinates.html)
- [Pattern Prophet](patterns.html)
- [Market Math](market.html) — ZMW change
- [Travel Graph Dash](travel.html)
- [Earth Geometry](earth.html)
- [LP Region Rush](lp.html)

No install. No build step.
"""
    (ROOT / "README.md").write_text(readme, encoding="utf-8")
    print("done")


if __name__ == "__main__":
    main()
