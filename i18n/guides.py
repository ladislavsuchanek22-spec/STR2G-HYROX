"""Anglické průvodce (guides) na str2g.com – článkové stránky s FAQ a kartami programů.

Volá se z i18n/build.py. Stránka s draft=True se negeneruje ani nepřidá do sitemap.
Zveřejnění: v GUIDES nastav draft=False a spusť python3 i18n/build.py.
"""
import json
from html import escape
from pages import BASE, T, card, faq_html, shead, ul, NET, extract  # noqa: F401
import programs

RULEBOOK = '<a href="https://hyrox.com/rulebook/" target="_blank" rel="noopener">HYROX rulebook</a>'

NEW = {
    "skierg": dict(
        draft=False, station=True,
        slug="/guides/hyrox-skierg/",
        date="2026-11-25",
        title="HYROX SkiErg: Technique, Pacing & Workouts for the First 1000 m | STR2G",
        desc="HYROX SkiErg guide: rules, damper setting, technique from the hips, common mistakes, how to pace 1000 m and workouts to train it with running.",
        eyebrow="HYROX station 1",
        h1=("SkiErg", "You won't win the race here. You can lose it."),
        lead="The SkiErg is station one. You arrive after the first kilometre, fresh and full of adrenaline. That is exactly why most people go out too hard and pay for it with a heart rate that never comes back down.",
        sections=[
            ("Rules", f"""<table class="lp-table"><thead><tr><th>Distance</th><th>Machine</th><th>Damper</th></tr></thead><tbody>
<tr><td>1000 m, every division</td><td>Concept2 SkiErg</td><td>Preset to 6, you may adjust it</td></tr>
</tbody></table>
<p class="lp-p">A judge resets the monitor before you start. Both feet stay on the base the whole time. You may lift your heels, but not step off. Rules change between seasons, so check the current {RULEBOOK} before race day.</p>"""),
            ("Technique: drop your body into it", """<ul class="lp-list">
<li><b>Start tall.</b> Hands up at forehead height, elbows slightly bent, trunk braced, shoulders down.</li>
<li><b>Catch with trunk and lats.</b> Brace your abs, press the handles down and let your body weight fall into them. The elbow angle barely changes.</li>
<li><b>Finish with a hip hinge, not a squat.</b> Hips travel back, knees bend only slightly, hands finish beside your thighs.</li>
<li><b>Recover slowly.</b> Stand back up along the same path. This is where you breathe in and rest.</li>
<li><b>Damper 5–7, 35–45 strokes per minute.</b> A higher damper is not faster, just heavier on the arms.</li>
</ul>"""),
            ("Common mistakes", """<ul class="lp-list">
<li><b>Arms-only pulling.</b> Your triceps and shoulders do all the work and fade by 400 m. Start every stroke by sending your hips back.</li>
<li><b>Squatting instead of hinging.</b> You burn the legs you need for the sleds.</li>
<li><b>Short, choppy strokes.</b> High stroke rate, no metres. Finish at your thighs and slow the recovery.</li>
<li><b>Going out too hot.</b> The first 200 m ten seconds too fast, then a heart rate that won't settle.</li>
<li><b>Damper on max</b> and <b>holding your breath.</b> Exhale loudly on every pull.</li>
</ul>"""),
            ("How to pace 1000 m", """<p class="lp-p">Ski 1000 m all out after a warm-up and note your average per 500 m. Add 5–8 seconds per 500 m: that is your race pace. A 4:00 test (2:00 / 500 m) gives a race pace of about 2:05–2:08 / 500 m.</p>
<ul class="lp-list">
<li><b>0–200 m:</b> settle in at target pace. Adrenaline will push you faster. Don't let it.</li>
<li><b>200–800 m:</b> same pace, same stroke rate, long strokes.</li>
<li><b>800–1000 m:</b> no sprint finish. Get your breathing under control and think about running.</li>
</ul>"""),
            ("Workouts", """<ol class="lp-steps">
<li><b>Race pace:</b> 6 × 500 m at race pace, 1 min rest. Every rep the same.</li>
<li><b>Speed reserve:</b> 10 × 200 m at 5 s / 500 m faster than race pace, 45 s rest.</li>
<li><b>Race start:</b> 1 km run + 1000 m SkiErg + 1 km run. The second kilometre should be as fast as the first.</li>
<li><b>Quick transitions:</b> 6 rounds of 250 m SkiErg + 400 m run, no rest.</li>
</ol>"""),
        ],
        picks=["basic", "competitor", "singles"],
        faq=[
            ("How long is the SkiErg in HYROX?", "1000 m in every division. It is the first station, straight after the first 1 km run."),
            ("What damper setting should I use on the HYROX SkiErg?", "The damper is preset to 6 and you are allowed to change it. Most athletes do best between 5 and 7. A higher setting makes the stroke heavier, not faster."),
            ("How fast should I ski in HYROX?", "Add 5–8 seconds per 500 m to your all-out 1000 m test. You should be able to run the next kilometre at your planned pace without walking."),
        ],
    ),
    "sled-push": dict(
        draft=False, station=True,
        slug="/guides/hyrox-sled-push/",
        date="2026-11-25",
        title="HYROX Sled Push: Weights, Technique & How to Pace 4 × 12.5 m | STR2G",
        desc="HYROX sled push guide: weights for every division, body position, short steps, where to rest, common mistakes and workouts to push faster and still run.",
        eyebrow="HYROX station 2",
        h1=("Sled push", "Low, braced and short steps."),
        lead="The sled push is the first real strength station. Four lengths of 12.5 m look short on paper. On carpet, with a heavy sled and two kilometres in your legs, this is where the second half of many races falls apart.",
        sections=[
            ("Weights and rules", f"""<table class="lp-table"><thead><tr><th>Division</th><th>Weight incl. sled</th><th>Distance</th></tr></thead><tbody>
<tr><td>Women Open</td><td>102 kg</td><td>4 × 12.5 m</td></tr>
<tr><td>Men Open / Women Pro</td><td>152 kg</td><td>4 × 12.5 m</td></tr>
<tr><td>Men Pro</td><td>202 kg</td><td>4 × 12.5 m</td></tr>
</tbody></table>
<p class="lp-p">The whole sled must cross the line before you turn. You can rest whenever you like, but the clock keeps running. Carpet differs between events, so the same weight can glide one day and stick the next. Check the current {RULEBOOK} before race day.</p>"""),
            ("Technique", """<ul class="lp-list">
<li><b>Arms are a rigid link.</b> Straight or bent, it doesn't matter, as long as the elbow angle doesn't change.</li>
<li><b>One line from head to heels.</b> Lean in, hips below shoulders, flat back, abs braced.</li>
<li><b>Short, quick steps</b> off the balls of your feet. Long strides lift you out of position and stall the sled.</li>
<li><b>Never stop mid-length.</b> Restarting a dead sled is the hardest part. Rest at the turns, where you stop anyway.</li>
<li><b>Grippy shoes.</b> Test your race shoes on carpet. A slipping foot costs power.</li>
</ul>"""),
            ("Common mistakes", """<ul class="lp-list">
<li><b>Hips too high:</b> you push with arms and shoulders and leg power never reaches the sled.</li>
<li><b>Flying the first length:</b> by length three you are standing still. All four lengths should take about the same time.</li>
<li><b>Rounded back:</b> leg power leaks away. If you can't keep a flat back, raise your grip.</li>
<li><b>Holding your breath:</b> exhale every second step.</li>
</ul>"""),
            ("Pacing: plan your rest", """<p class="lp-p">The sled is not about never stopping. It is about stopping briefly, in the right place, with a plan. Ten seconds at the turn beats thirty in the middle of a length. Example plan: length, three breaths at the turn, length, three breaths, length, five breaths, final length.</p>
<p class="lp-p">The first few hundred metres after the sled are the hardest running of the race. Shorten your stride, lift your cadence and don't panic. It settles within 300 m.</p>"""),
            ("Workouts", """<ol class="lp-steps">
<li><b>Light technique:</b> 8 × 12.5 m at 70% of race weight, 60 s rest.</li>
<li><b>Heavy lengths:</b> 6 × 12.5 m at race weight +20–30 kg, 2 min rest.</li>
<li><b>Station two:</b> 1 km run + 50 m sled push + 1 km run. The second kilometre no more than 10–15 s slower.</li>
<li><b>Heavy legs:</b> 3 rounds of 25 m push + 20 walking lunges + 600 m run.</li>
</ol>"""),
        ],
        picks=["basic", "competitor", "singles"],
        faq=[
            ("How heavy is the HYROX sled push?", "Including the sled: 102 kg for Women Open, 152 kg for Men Open and Women Pro, 202 kg for Men Pro. Four lengths of 12.5 m, 50 m in total."),
            ("How do I push the sled faster in HYROX?", "Get low with a flat back, use short quick steps, keep the sled moving through each length and take planned rests only at the turns."),
            ("Can I rest during the sled push?", "Yes, but plan it. Short rests at the turns are much cheaper than stopping mid-length and restarting a dead sled."),
        ],
    ),
    "burpee-broad-jumps": dict(
        draft=False, station=True,
        slug="/guides/hyrox-burpee-broad-jumps/",
        date="2026-11-25",
        title="HYROX Burpee Broad Jumps: Rules, Technique & Pacing for 80 m | STR2G",
        desc="HYROX burpee broad jumps: the movement standard, an economical rep, jump length, breathing, common no-reps and workouts to hold one rhythm for 80 m.",
        eyebrow="HYROX station 4",
        h1=("Burpee broad jumps", "Strength doesn't win here. Rhythm does."),
        lead="Station four and, for many people, the worst one. No equipment, just you, the floor and 80 metres after both sleds. Fly through the first twenty metres and you will be lying on the floor at halfway.",
        sections=[
            ("Rules", f"""<ul class="lp-list">
<li>80 m in every division, bodyweight only.</li>
<li>Your chest touches the floor on every burpee.</li>
<li>Your hands go down no more than one foot length in front of your toes.</li>
<li>Take-off and landing are two-footed, feet side by side. No steps forward between landing and the next burpee.</li>
</ul>
<p class="lp-p">Check the current {RULEBOOK} before race day.</p>"""),
            ("Technique: the same rep every time", """<ul class="lp-list">
<li><b>Down:</b> hands just in front of your toes, feet back, chest on the floor. Don't crash, don't brake with your arms.</li>
<li><b>Up:</b> stepping up is slower but saves heart rate. Jumping up is faster and costs more. Test both after 40 m.</li>
<li><b>Jump forward, not up,</b> at about 70–80% of your max. Land softly on your whole foot.</li>
<li><b>Breathe:</b> out on the way down, in on the way up. If you must rest, rest standing.</li>
</ul>"""),
            ("Common mistakes", """<ul class="lp-list">
<li><b>Max-effort jumps:</b> every jump is a show, after 30 m you have nothing left.</li>
<li><b>Hands too far forward</b> or a <b>one-foot take-off:</b> risk of no-reps.</li>
<li><b>Lying on the floor</b> between reps. The seconds pile up.</li>
<li><b>Sprinting the start:</b> the second half takes twice as long.</li>
</ul>"""),
            ("Pacing: count jumps, not metres", """<p class="lp-p">Do 80 m fresh at a pace you can hold and count your jumps. 44 jumps means 11 for every 20 m. On race day you count to eleven, four times, and ignore how far is left.</p>
<p class="lp-p">After the burpees your heart rate is the highest of the race. Run the first 200 m a little slower. The good news: the next station is the row, where you sit down.</p>"""),
            ("Workouts", """<ol class="lp-steps">
<li><b>Race rhythm:</b> 4 × 40 m at race rhythm, 90 s rest. Same jump count every rep.</li>
<li><b>10-min EMOM:</b> 6–8 burpee broad jumps every minute.</li>
<li><b>Station four:</b> 1 km run + 80 m burpee broad jumps + 1 km run, no walking.</li>
<li><b>After the sled:</b> 3 rounds of 25 m sled pull + 400 m run + 30 m burpee broad jumps + 400 m run.</li>
</ol>"""),
        ],
        picks=["basic", "competitor", "singles"],
        faq=[
            ("How far are the burpee broad jumps in HYROX?", "80 m in every division. It is station four, after the sled push and sled pull."),
            ("What are the rules for HYROX burpee broad jumps?", "Chest to the floor on every rep, hands no further than one foot length in front of your toes, and a two-footed take-off and landing with no steps forward between reps."),
            ("Should I step or jump up in the burpees?", "Test both in training. Stepping up is slower per rep but keeps your heart rate lower, and many athletes are faster overall with it."),
        ],
    ),
    "rowing": dict(
        draft=False, station=True,
        slug="/guides/hyrox-rowing/",
        date="2026-11-25",
        title="HYROX Rowing: Technique, Damper & How to Pace the 1000 m Row | STR2G",
        desc="HYROX row guide: legs-body-arms technique, damper and stroke rate, common mistakes, how to pace 1000 m at halfway and workouts with running.",
        eyebrow="HYROX station 5",
        h1=("Rowing", "Halfway. Reset your breathing."),
        lead="The row is station five and exactly halfway. It is the only place in the race where you sit down. Use it to settle your breathing and set up the second half, or wreck yourself completely.",
        sections=[
            ("Rules", f"""<p class="lp-p">1000 m on a Concept2 rower in every division. A judge resets the monitor, you get up only after the full distance. The damper is preset and you may adjust it. Set your foot straps as soon as you sit down. Check the current {RULEBOOK} before race day.</p>"""),
            ("Technique: legs, body, arms", """<ul class="lp-list">
<li><b>Catch:</b> shins roughly vertical, arms straight, slight forward lean from the hips, flat back.</li>
<li><b>Drive:</b> push with the legs first. Only when they are almost straight swing the torso back, then pull the handle.</li>
<li><b>Finish:</b> handle at your lower ribs, torso just past vertical.</li>
<li><b>Recovery:</b> arms, body, then knees. Twice as long as the drive. This is where you rest.</li>
<li><b>Damper 4–6, 24–30 strokes per minute.</b> Breathe out on the drive.</li>
</ul>"""),
            ("Common mistakes", """<ul class="lp-list">
<li><b>Arms before legs:</b> your strongest muscles barely work.</li>
<li><b>Knees before hands</b> on the recovery: the handle loops over your knees.</li>
<li><b>Short, fast strokes:</b> high rate, no power.</li>
<li><b>Leaning back too far</b> or a <b>rounded back.</b></li>
</ul>"""),
            ("How to pace 1000 m", """<p class="lp-p">Row 1000 m all out after a warm-up. Add 6–10 seconds per 500 m to your average: that is your race pace. A 3:40 test (1:50 / 500 m) gives about 1:56–2:00 / 500 m.</p>
<ul class="lp-list">
<li><b>0–200 m:</b> three or four short strokes to spin the flywheel, then long strokes at target pace.</li>
<li><b>200–800 m:</b> hold it. This is where your body recovers most.</li>
<li><b>800–1000 m:</b> no sprint. Loosen the straps in the last metres so you can get straight off.</li>
</ul>"""),
            ("Workouts", """<ol class="lp-steps">
<li><b>Race pace:</b> 6 × 500 m at race pace, 1 min rest.</li>
<li><b>Rate ladder:</b> 4 × 4 min, 1 min each at 22–24–26–28 strokes per minute.</li>
<li><b>Station five:</b> 1 km run + 1000 m row + 1 km run.</li>
<li><b>Row and farmers:</b> 4 rounds of 500 m row + 100 m farmers carry + 400 m easy run.</li>
</ol>"""),
        ],
        picks=["basic", "competitor", "raceprep"],
        faq=[
            ("How long is the row in HYROX?", "1000 m on a Concept2 rower in every division. It is station five, exactly halfway through the race."),
            ("What damper should I use for the HYROX row?", "Most athletes do best between 4 and 6. Train on the setting you will race on. A higher damper makes each stroke heavier, not faster."),
            ("How fast should I row in HYROX?", "Add 6–10 seconds per 500 m to your all-out 1000 m test. Leave the rower ready to run, not wrecked."),
        ],
    ),
    "farmers-carry": dict(
        draft=False, station=True,
        slug="/guides/hyrox-farmers-carry/",
        date="2026-11-25",
        title="HYROX Farmers Carry: Weights, Grip & How to Carry 200 m Unbroken | STR2G",
        desc="HYROX farmers carry guide: kettlebell weights, pick-up, posture, grip, walk or shuffle, where to put them down and workouts for grip under fatigue.",
        eyebrow="HYROX station 6",
        h1=("Farmers carry", "The fastest station. If your hands hold out."),
        lead="Two kettlebells, 200 metres. Done well, it takes around two minutes. The catch is what comes before it: your grip has already worked on the sled pull and the rower.",
        sections=[
            ("Weights and rules", f"""<table class="lp-table"><thead><tr><th>Division</th><th>Kettlebells</th><th>Distance</th></tr></thead><tbody>
<tr><td>Women Open</td><td>2 × 16 kg</td><td>200 m</td></tr>
<tr><td>Men Open / Women Pro</td><td>2 × 24 kg</td><td>200 m</td></tr>
<tr><td>Men Pro</td><td>2 × 32 kg</td><td>200 m</td></tr>
</tbody></table>
<p class="lp-p">You can put the kettlebells down at any time and continue from there. Walking and running are both allowed. Check the current {RULEBOOK} before race day.</p>"""),
            ("Technique: chest up, load quiet", """<ul class="lp-list">
<li><b>Pick up like a deadlift:</b> bend at hips and knees, flat back, brace.</li>
<li><b>Posture:</b> chest up, shoulders down and slightly back, arms hanging long, eyes forward.</li>
<li><b>Short, quick steps.</b> A fast walk or light shuffle, whichever keeps the bells from swinging.</li>
<li><b>Grip:</b> handle deep in the palm, thumb locked over the fingers. Firm, not maximal.</li>
<li><b>Dry hands:</b> wipe your palms before the station.</li>
</ul>"""),
            ("Common mistakes", """<ul class="lp-list">
<li><b>Shrugged shoulders:</b> traps and neck tire in a few dozen metres.</li>
<li><b>Long strides:</b> the bells swing and hit your thighs.</li>
<li><b>Death grip</b> from the first metre: your forearms go at halfway.</li>
<li><b>Dropping only at failure:</b> put them down a few metres earlier than you have to, three breaths, go.</li>
</ul>"""),
            ("Pacing: unbroken, or a plan", """<p class="lp-p">There is little to gain here and a lot to lose. The ideal is 200 m without putting down, at a fast, quiet walk. If your grip can't do that, decide your breaks in advance: 100 + 100 or 80 + 60 + 60. One planned break beats three forced ones. Never put down in the last 50 m.</p>"""),
            ("Workouts", """<ol class="lp-steps">
<li><b>200 m test:</b> race weight, unbroken. Note your time and where you put down.</li>
<li><b>Grip:</b> 4 rounds of 30 s dead hang + 40 m carry at race weight.</li>
<li><b>Station six:</b> 1 km run + 200 m farmers carry + 1 km run.</li>
<li><b>Grip under fatigue:</b> 3 rounds of 12.5 m sled pull + 100 m carry + 400 m run.</li>
</ol>"""),
        ],
        picks=["basic", "competitor", "singles"],
        faq=[
            ("How heavy is the HYROX farmers carry?", "Two kettlebells of 16 kg for Women Open, 24 kg for Men Open and Women Pro, 32 kg for Men Pro. The distance is 200 m."),
            ("Can I put the kettlebells down during the farmers carry?", "Yes, as often as you need, and you continue from where you put them down. Plan short breaks rather than waiting until your grip fails."),
            ("Should I run or walk the farmers carry?", "Whichever keeps the kettlebells quiet. A fast walk with short steps works for most athletes. A shuffle is quicker but swings the load and raises your heart rate."),
        ],
    ),
    "sandbag-lunges": dict(
        draft=False, station=True,
        slug="/guides/hyrox-sandbag-lunges/",
        date="2026-11-25",
        title="HYROX Sandbag Lunges: Weights, Standard & How to Pace 100 m | STR2G",
        desc="HYROX sandbag lunges: bag weights, the knee-touch standard, stride length, breathing, how to split 100 m and workouts to survive station seven.",
        eyebrow="HYROX station 7",
        h1=("Sandbag lunges", "This is where the race really starts."),
        lead="Seven kilometres and six stations in your legs, then a sandbag on your shoulders and 100 metres of lunges. Every step is a rep and none of them is free.",
        sections=[
            ("Weights and rules", f"""<table class="lp-table"><thead><tr><th>Division</th><th>Sandbag</th><th>Distance</th></tr></thead><tbody>
<tr><td>Women Open</td><td>10 kg</td><td>100 m</td></tr>
<tr><td>Men Open / Women Pro</td><td>20 kg</td><td>100 m</td></tr>
<tr><td>Men Pro</td><td>30 kg</td><td>100 m</td></tr>
</tbody></table>
<p class="lp-p">The bag stays on your shoulders the whole time. The back knee touches the floor on every lunge and you stand up fully each time. Alternate legs with no extra steps. You can rest standing with the bag on. Check the current {RULEBOOK} before race day.</p>"""),
            ("Technique: upright and smooth", """<ul class="lp-list">
<li><b>Bag high on your shoulders,</b> elbows forward. Your hands steady it, they don't carry it.</li>
<li><b>Medium step:</b> front shin roughly vertical, back knee lowers under control and touches lightly.</li>
<li><b>Stand tall</b> through the whole front foot, lock out briefly, straight into the next step.</li>
<li><b>One lunge, one breath:</b> in on the way down, out on the way up.</li>
</ul>"""),
            ("Common mistakes", """<ul class="lp-list">
<li><b>Tiny steps:</b> dozens of extra reps for the same distance.</li>
<li><b>Leaning forward:</b> the bag presses on your neck and your back takes over.</li>
<li><b>Not standing tall:</b> you risk no-reps.</li>
<li><b>Going out too hot</b> and then <b>long standing breaks.</b> A break is three breaths, no more.</li>
</ul>"""),
            ("Pacing: a rhythm you can hold", """<p class="lp-p">On the lunges, the athlete who doesn't stop wins. A slower continuous rhythm almost always beats fast bursts with long breaks. Example plan: 25 m, three breaths, 25 m, three breaths, 25 m, three breaths, final 25 m without stopping.</p>
<p class="lp-p">Afterwards your legs feel like rubber. Run off with a short stride and forget pace for 200 m. You need those legs for 100 wall balls.</p>"""),
            ("Workouts", """<ol class="lp-steps">
<li><b>Race sections:</b> 4 × 50 m at race weight, unbroken, 90 s rest.</li>
<li><b>Leg strength:</b> 4 rounds of 8 Bulgarian split squats per leg + 10 goblet squats + 30 s plank.</li>
<li><b>Station seven:</b> 1 km run + 100 m lunges + 1 km run.</li>
<li><b>Lunges and wall balls:</b> 3 rounds of 50 m lunges + 400 m run + 25 wall balls.</li>
</ol>"""),
        ],
        picks=["basic", "competitor", "raceprep"],
        faq=[
            ("How heavy is the HYROX sandbag?", "10 kg for Women Open, 20 kg for Men Open and Women Pro, 30 kg for Men Pro. The distance is 100 m."),
            ("Does the knee have to touch the floor in HYROX lunges?", "Yes. The back knee touches the floor on every lunge and you stand up fully between reps."),
            ("How do I get faster at HYROX sandbag lunges?", "Use a medium stride you can repeat, stay upright, and hold one continuous rhythm with short planned breaks instead of fast bursts and long stops."),
        ],
    ),
}


GUIDES = {
    "hyrox-taper": dict(
        draft=False,
        slug="/guides/hyrox-taper/",
        date="2026-10-26",
        title="HYROX Taper: How to Taper for a HYROX Race (2-Week Plan) | STR2G",
        desc="How to taper for HYROX: what to cut, what to keep, a 2-week taper outline and race week checklist. From HYROX coaches who race themselves.",
        eyebrow="HYROX guide",
        h1=("HYROX taper", "Fresh legs, sharp engine."),
        lead="The last two weeks before a HYROX race decide whether you arrive fresh or flat. You can't build fitness now. You can only lose it or protect it. A good taper protects it.",
        sections=[
            ("What a taper is", """<p class="lp-p">A taper is a planned drop in training volume before a race while you keep the intensity. Less total work, same quality. Fatigue goes down faster than fitness, so you arrive at the start line rested and still sharp.</p>"""),
            ("What to cut and what to keep", """<ul class="lp-list">
<li><b>Cut volume:</b> roughly 30–50% less total running distance and fewer station sets than in your peak weeks.</li>
<li><b>Keep intensity:</b> short efforts at race pace and slightly faster, so your body remembers the speed.</li>
<li><b>Keep frequency:</b> train on similar days as before. Fewer sessions often make people feel sluggish.</li>
<li><b>Drop heavy new stimuli:</b> no max-effort lifts, no new exercises, no full race simulations.</li>
</ul>"""),
            ("A 2-week taper outline", """<table class="lp-table"><thead><tr><th>When</th><th>Focus</th><th>Example</th></tr></thead><tbody>
<tr><td>Week −2</td><td>Volume down, intensity kept</td><td>Run intervals at race pace, half-size station blocks, one shorter compromised run session</td></tr>
<tr><td>Week −1, early</td><td>Sharpen</td><td>Short race-pace runs (e.g. 4 × 400 m), a few reps on sleds and wall balls at race weight</td></tr>
<tr><td>2–3 days out</td><td>Prime</td><td>20–30 min easy, a few strides, mobility</td></tr>
<tr><td>Day before</td><td>Rest or shake-out</td><td>10–20 min easy jog, pack your bag, sleep</td></tr>
</tbody></table>
<p class="lp-p">Our <a href="/programs/hyrox-taper/">2-Week HYROX Taper</a> program has every session written out for Open, Doubles and Pro.</p>"""),
            ("Race week checklist", """<ul class="lp-list">
<li>Sleep more than usual, especially two nights before the race.</li>
<li>Eat normally with a bit more carbohydrate in the last two days. Nothing new.</li>
<li>Check your start time, division and the latest rulebook.</li>
<li>Pack shoes and kit you have trained in.</li>
<li>Plan your pacing: first two runs slower than you want.</li>
</ul>"""),
        ],
        picks=["taper", "singles", "raceprep"],
        faq=[
            ("How long should a HYROX taper be?", "Most athletes do well with 7–14 days. Beginners racing their first HYROX can use about one week, athletes after a long, heavy block often benefit from two."),
            ("Should I stop training before HYROX?", "No. Keep training, but do less. Stopping completely often makes you feel flat on race day. Reduce volume and keep short, sharp efforts."),
            ("Should I do a full HYROX simulation in race week?", "No. A full simulation takes days to recover from. Keep it to short parts of the race at race pace."),
            ("What should I eat before a HYROX race?", "A light, carb-based meal 2–3 hours before your start that you have tested in training. Avoid new foods on race day."),
        ],
    ),
    "compromised-running": dict(
        draft=False,
        slug="/guides/hyrox-compromised-running/",
        date="2026-10-26",
        title="Compromised Running for HYROX: Workouts to Run Fast on Tired Legs | STR2G",
        desc="Compromised running is running right after a station. Why it decides your HYROX time, how to pace it and 5 workouts to train it.",
        eyebrow="HYROX guide",
        h1=("Compromised running", "Run fast on tired legs."),
        lead="In HYROX you never run fresh. Every kilometre after the first comes straight off a station. Training that is the single biggest lever for most athletes.",
        sections=[
            ("What compromised running is", """<p class="lp-p">Compromised running means running under fatigue from another effort: after sleds, burpees, lunges or wall balls. Your legs are heavy, your heart rate is high and your stride shortens. Athletes who only train fresh running often lose minutes on the second half of the race.</p>"""),
            ("How to pace it", """<ul class="lp-list">
<li>Start each run slightly slower than race pace for the first 100–200 m, then settle into your pace.</li>
<li>Use short, quick steps until your legs come back. Don't fight for long strides.</li>
<li>Control your breathing first. Speed follows.</li>
<li>Keep the Roxzone short: run into the station, run out of it.</li>
</ul>"""),
            ("5 compromised running workouts", """<ol class="lp-steps">
<li><b>Sled to run:</b> 4 rounds of 25 m sled push + 1 km at race pace. Rest 2 minutes.</li>
<li><b>Lunge to run:</b> 4 rounds of 50 m sandbag lunges + 800 m. The run after lunges is the hardest in the race.</li>
<li><b>Wall ball finisher:</b> 3 rounds of 1 km + 30 wall balls, no rest between.</li>
<li><b>Machine combo:</b> 5 rounds of 500 m row or SkiErg + 600 m run at race pace.</li>
<li><b>Half race:</b> 4 × (1 km + a station) at race pace, 4–6 weeks before the race.</li>
</ol>"""),
            ("How often to train it", """<p class="lp-p">One or two compromised running sessions a week is enough for most athletes, next to easy running and strength. More is not better here. These sessions are hard and need recovery. If running is your weak point, our <a href="/programs/running-for-hyrox/">Running for HYROX</a> program builds it over 12 weeks.</p>"""),
        ],
        picks=["running", "competitor", "basic"],
        faq=[
            ("What is compromised running in HYROX?", "Running right after a station, on tired legs and with a high heart rate. In HYROX every kilometre after the first is compromised."),
            ("How do I get better at running after sleds?", "Train it directly: short sled pushes or pulls followed by 1 km at race pace. Add strength work for legs twice a week and keep an easy running base."),
            ("How many compromised running sessions per week?", "One or two for most athletes, alongside easy runs and strength training."),
        ],
    ),
    "sled-pull": dict(
        draft=False, station=True,
        slug="/guides/hyrox-sled-pull-technique/",
        date="2026-10-26",
        title="HYROX Sled Pull Technique: How to Pull Faster and Save Your Legs | STR2G",
        desc="How to improve your HYROX sled pull: technique, rope handling, weights for every division and workouts to get faster. From HYROX coaches.",
        eyebrow="HYROX guide",
        h1=("Sled pull", "Pull with your legs, not your arms."),
        lead="The sled pull is station three. 50 metres, pulled in by rope. Most people lose time here because they pull with their arms and burn out their grip before the next run.",
        sections=[
            ("Weights and rules", """<table class="lp-table"><thead><tr><th>Division</th><th>Total sled weight</th><th>Distance</th></tr></thead><tbody>
<tr><td>Women Open</td><td>78 kg</td><td>50 m</td></tr>
<tr><td>Men Open / Women Pro</td><td>103 kg</td><td>50 m</td></tr>
<tr><td>Men Pro</td><td>153 kg</td><td>50 m</td></tr>
</tbody></table>
<p class="lp-p">You stay standing in the athlete box, pull the whole sled past the line, then run to the other end and pull it back. Missing a length is an incomplete station and a DQ. Source: <a href="https://hyrox.com/rulebook/" target="_blank" rel="noopener">HYROX Singles Rulebook 2026/27</a>. Always check the current rulebook before your race.</p>"""),
            ("Technique", """<ul class="lp-list">
<li><b>Sit back and drive with the legs.</b> Low hips, lean back, and push through your heels. Your arms just transfer the force.</li>
<li><b>Hand over hand, short and fast.</b> Long pulls look strong but kill your grip.</li>
<li><b>Keep the sled moving.</b> Restarting a stopped sled costs far more than keeping it rolling.</li>
<li><b>Manage the rope.</b> Let it pile behind you, not under your feet.</li>
<li><b>Breathe.</b> Exhale with every pull. Holding your breath spikes your heart rate before the burpees.</li>
</ul>"""),
            ("Workouts to get faster", """<ol class="lp-steps">
<li><b>Technique:</b> 4 × 12.5 m at moderate weight, focus on leg drive.</li>
<li><b>Race weight:</b> 3 × 25 m at race weight, 2 minutes rest.</li>
<li><b>Under fatigue:</b> 1 km run + 25 m sled push + 25 m sled pull, 3 rounds.</li>
<li><b>Strength:</b> rows, deadlifts and farmers carries twice a week for back and grip.</li>
</ol>
<p class="lp-p">All eight stations are built into our <a href="/programs/hyrox-basic/">HYROX Basic</a> and <a href="/programs/hyrox-competitor/">HYROX Competitor</a> programs.</p>"""),
        ],
        picks=["basic", "competitor", "singles"],
        faq=[
            ("How heavy is the HYROX sled pull?", "Total sled weight is 78 kg for Women Open, 103 kg for Men Open and Women Pro, and 153 kg for Men Pro. Distance is 50 m in every division."),
            ("How do I improve my HYROX sled pull?", "Pull with your legs, not your arms: sit back, drive through your heels and use short, quick hand-over-hand pulls. Train it at race weight after runs and build back and grip strength."),
            ("Should I wear gloves for the sled pull?", "Many athletes do. Gloves are allowed in HYROX (grips are not). Test them in training first."),
        ],
    ),
    "doubles": dict(
        draft=False,
        slug="/guides/hyrox-doubles-training/",
        date="2026-11-01",
        title="HYROX Doubles Training: Rules, Splitting Stations & Partner Workouts | STR2G",
        desc="How HYROX Doubles works, how to split the stations with your partner and 4 partner workouts to train together. From coaches who race Mixed Doubles.",
        eyebrow="HYROX guide",
        h1=("HYROX Doubles", "Two athletes, one race plan."),
        lead="Doubles is the best way into HYROX and one of the most fun ways to race it. You both run the full 8 km, but you split the work on the stations. The teams that do well are not always the fittest. They are the ones with a plan.",
        sections=[
            ("How Doubles works", """<ul class="lp-list">
<li><b>You both run everything.</b> All 8 × 1 km, side by side.</li>
<li><b>You split the stations.</b> Any way you like, as long as the full distance or rep count is done before you leave.</li>
<li><b>You stay together.</b> You run every kilometre together and enter and leave each station together. If one of you runs ahead, it's a 1-minute penalty, and more than three of those puts you out of competition.</li>
<li><b>Divisions:</b> Women, Men, Mixed and Doubles Pro.</li>
<li><b>Weights:</b> the same as the matching singles division (Women Open, Men Open, Pro).</li>
</ul>
<p class="lp-p">Always check the current HYROX rulebook for your race before you start.</p>"""),
            ("How to split the stations", """<ul class="lp-list">
<li><b>SkiErg and row:</b> short pieces, e.g. 250 m each, and switch. Swaps on a machine are quick, so short hard efforts win.</li>
<li><b>Sleds:</b> switch every length (12.5 m). The stronger partner can do more, but not so much that they die on the next run.</li>
<li><b>Burpee broad jumps:</b> short sections so you both keep the same rhythm.</li>
<li><b>Farmers carry and lunges:</b> switch at lines or markers on the course.</li>
<li><b>Wall balls:</b> sets of 10–15. Short sets and fast hand-overs beat long sets with long breaks at the end of a race.</li>
</ul>"""),
            ("4 partner workouts", """<ol class="lp-steps">
<li><b>Race-pace run together:</b> 4 × 1 km at your shared race pace, 90 s rest. The slower partner sets the pace.</li>
<li><b>You go, I go:</b> 10 rounds of 15 wall balls each, one works while the other rests.</li>
<li><b>Mini simulation:</b> 4 × (1 km run + one station, split), practising your hand-overs.</li>
<li><b>Sled relay:</b> 8 × 12.5 m push and pull, switching every length.</li>
</ol>
<p class="lp-p">Our <a href="/programs/8-week-hyrox-doubles/">8-Week HYROX Doubles</a> program gives both partners a full plan with running, strength and partner sessions.</p>"""),
        ],
        picks=["doubles", "basic", "running"],
        faq=[
            ("Do both partners run the full distance in HYROX Doubles?", "Yes. Both partners run all 8 × 1 km together. Only the station work is split."),
            ("How should we split the stations in HYROX Doubles?", "There is no 50/50 rule. Use short pieces on SkiErg and row, switch every length on the sleds and do wall balls in sets of 10–15."),
            ("What weights are used in HYROX Doubles?", "The same as the matching singles division: Women Doubles use Women Open weights, Men and Mixed use Men Open weights, Doubles Pro uses Pro weights."),
        ],
    ),
    "running": dict(
        draft=False,
        slug="/guides/how-to-run-faster-in-hyrox/",
        title="How to Run Faster in HYROX: Running Training for Hybrid Racing | STR2G",
        desc="Running is half of your HYROX time. How to build your running for HYROX: easy base, threshold work, compromised runs and pacing the 8 × 1 km.",
        eyebrow="HYROX guide",
        h1=("Run faster in HYROX", "Half the race is running."),
        lead="Eight kilometres doesn't sound like much. But in HYROX you run it in eight pieces, after every station, on tired legs. Running is roughly half of your race time, and it's where most athletes have the biggest room to improve.",
        sections=[
            ("Why running decides HYROX", """<p class="lp-p">Stations feel hard, but they are short. You spend more time running than on any single station, and every kilometre after the first is run on tired legs. Losing 20 seconds on every run adds up to more than 2.5 minutes. Most athletes can find that time in running faster than in getting stronger.</p>"""),
            ("The building blocks", """<ul class="lp-list">
<li><b>Easy base:</b> most of your running should be easy, at a pace where you could hold a conversation. It builds the engine without wrecking your legs for strength days.</li>
<li><b>Threshold work:</b> once a week, longer intervals at a comfortably hard pace, e.g. 3–5 × 1 km or 2–3 × 10 min.</li>
<li><b>Compromised running:</b> runs straight after a station. See our <a href="/guides/hyrox-compromised-running/">compromised running guide</a>.</li>
<li><b>Strength:</b> squats, lunges and calf work twice a week keep your legs running after sleds and lunges.</li>
</ul>"""),
            ("Pacing the 8 × 1 km", """<ul class="lp-list">
<li>Run the first two kilometres slower than you want to. Everyone goes out too fast.</li>
<li>Aim for even splits. A big drop-off in runs 6–8 means you went too hard early.</li>
<li>Use the Roxzone: jog, don't walk. It counts towards your time.</li>
</ul>"""),
            ("A simple running week", """<table class="lp-table"><thead><tr><th>Day</th><th>Session</th></tr></thead><tbody>
<tr><td>Mon</td><td>Easy run 30–45 min</td></tr>
<tr><td>Wed</td><td>Threshold: 4 × 1 km, 90 s rest</td></tr>
<tr><td>Fri</td><td>Compromised: 4 × (station + 1 km)</td></tr>
<tr><td>Sun</td><td>Long easy run 45–70 min</td></tr>
</tbody></table>
<p class="lp-p">Combine it with 2 strength sessions. Our <a href="/programs/running-for-hyrox/">Running for HYROX</a> program builds this up week by week.</p>"""),
        ],
        picks=["running", "basic", "singles"],
        faq=[
            ("How much of a HYROX race is running?", "You run 8 × 1 km. For most athletes running takes roughly half of the total race time."),
            ("How many times a week should I run for HYROX?", "Three to four runs a week works for most athletes: mostly easy running, one threshold session and one compromised session."),
            ("How do I pace the runs in HYROX?", "Start the first two runs slower than you feel like and aim for even splits. Fading badly in the last three runs means you started too fast."),
        ],
    ),
    "wall-balls": dict(
        draft=True, station=True,
        slug="/guides/hyrox-wall-balls/",
        title="HYROX Wall Balls: Standards, Technique & How to Pace 100 Reps | STR2G",
        desc="HYROX wall balls: ball weights and target heights for every division, the movement standard, technique that saves your legs and how to split 100 reps.",
        eyebrow="HYROX guide",
        h1=("Wall balls", "The last 100 reps."),
        lead="Wall balls are the final station. 100 reps after 7 km of running and seven stations. This is where races are won and lost, and where most no-reps happen.",
        sections=[
            ("Weights and target heights", """<table class="lp-table"><thead><tr><th>Division</th><th>Ball</th><th>Target</th></tr></thead><tbody>
<tr><td>Women Open</td><td>4 kg</td><td>2.70 m</td></tr>
<tr><td>Women Pro</td><td>6 kg</td><td>2.70 m</td></tr>
<tr><td>Men Open</td><td>6 kg</td><td>3.00 m</td></tr>
<tr><td>Men Pro</td><td>9 kg</td><td>3.00 m</td></tr>
</tbody></table>
<p class="lp-p">Every rep starts standing. Squat until your hip crease is below your knees, then throw the ball with both hands into the target zone. Shallow squats and misses don't count. There are no warnings here, it's a rep or a no-rep, and leaving before 100 valid reps is an incomplete station and a DQ. Source: <a href="https://hyrox.com/rulebook/" target="_blank" rel="noopener">HYROX Singles Rulebook 2026/27</a>.</p>"""),
            ("Technique that saves you", """<ul class="lp-list">
<li><b>Ball at your chin, elbows under it.</b> When the ball drops to your waist, every throw costs more.</li>
<li><b>Throw with your legs.</b> Drive up from the squat. The arms only finish the throw.</li>
<li><b>Catch straight into the squat.</b> One fluid movement, no standing with the ball.</li>
<li><b>Stand an arm's length from the wall.</b> Too close and the ball hits your face, too far and you miss low.</li>
<li><b>Breathe with the rhythm.</b> Exhale on the throw, inhale on the catch.</li>
</ul>"""),
            ("How to split 100 reps", """<ul class="lp-list">
<li><b>Strong:</b> 25-25-20-15-15 with short breaks.</li>
<li><b>Solid:</b> 5 × 20, 10–15 s breaks.</li>
<li><b>First race:</b> 10 × 10, breathe between sets, never more than 15 s.</li>
</ul>
<p class="lp-p">Start your breaks before you have to. Short planned breaks are faster than long forced ones.</p>"""),
            ("Workouts", """<ol class="lp-steps">
<li><b>Under fatigue:</b> 1 km run + 100 m lunges + 50 wall balls, 2 rounds.</li>
<li><b>EMOM:</b> 10 minutes, 15 wall balls every minute at race weight.</li>
<li><b>Strength:</b> front squats and thrusters twice a week.</li>
</ol>"""),
        ],
        picks=["basic", "competitor", "singles"],
        faq=[
            ("How many wall balls are in HYROX?", "100 reps in every division. It is the last station."),
            ("What is the wall ball weight in HYROX?", "4 kg for Women Open, 6 kg for Women Pro and Men Open, 9 kg for Men Pro. Women throw to 2.70 m, men to 3.00 m."),
            ("How should I split 100 wall balls?", "Plan sets before the race: 5 × 20 or 10 × 10 with short breaks works for most athletes. Rest before you are forced to."),
        ],
    ),
}


GUIDES.update(NEW)

# Pořadí stanic jako v závodě (pro odkazy „další stanice“ a landing page průvodce)
STATION_ORDER = ["skierg", "sled-push", "sled-pull", "burpee-broad-jumps", "rowing", "farmers-carry", "sandbag-lunges", "wall-balls"]

SG_LANDING = {"en": "/station-guide/", "cs": "/cs/pruvodce-stanicemi/"}


def sg_cta():
    """Blok s nabídkou celého průvodce (PDF) na stránkách stanic."""
    return '''
<section class="sg-cta">
  <div class="wrap">
    <div class="sg-box">
      <p class="eyebrow">Free PDF · 64 pages</p>
      <h2 class="display">All 8 stations.<br><span class="gold">One guide.</span></h2>
      <p class="lead">Technique, common mistakes, race pacing and 12 workouts for every station, from SkiErg to Wall Balls. Written by HYROX coaches who race themselves.</p>
      <div class="cta-row"><button type="button" class="btn btn-gold" data-sg-cta>Get the free Station Guide</button><a class="btn btn-ghost" href="/station-guide/">What's inside</a></div>
    </div>
  </div>
</section>'''


def station_nav(key):
    """Odkazy na ostatní stanice."""
    links = []
    for k in STATION_ORDER:
        g = GUIDES.get(k)
        if not g or g.get("draft"):
            continue
        label = NAV_LABELS.get(k, k)
        links.append(f'<span aria-current="page">{escape(label)}</span>' if k == key else f'<a href="{g["slug"]}">{escape(label)}</a>')
    return '<nav class="st-nav" aria-label="HYROX stations"><p class="eyebrow">All HYROX stations</p><div>' + "".join(links) + "</div></nav>"


def page(g, parts, key=None):
    tracking, style, fonts, verify, icons = parts
    u = T["en"]["ui"]
    url = BASE + g["slug"]
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "STR2G HYROX", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": g["h1"][0], "item": url}]},
        {"@type": "Article", "headline": g["title"].split(" | ")[0], "description": g["desc"], "inLanguage": "en",
         "mainEntityOfPage": url, "image": BASE + "/img/lada-ria-finish-line.jpg",
         **({"datePublished": g["date"], "dateModified": g.get("updated", g["date"])} if g.get("date") else {}),
         "author": [{"@type": "Person", "@id": "https://www.ladislavsuchanek.cz/#person", "name": "Ladislav Suchánek", "url": "https://www.ladislavsuchanek.cz/"},
                    {"@type": "Person", "@id": "https://riahrusovska.cz/#ria", "name": "Ria Suchánek Hrušovská", "url": "https://riahrusovska.cz/"}],
         "publisher": {"@type": "Organization", "@id": BASE + "/#org", "name": "STR2G HYROX", "url": BASE + "/"}},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in g["faq"]]},
    ]}
    secs = "".join(f'''
<section>
  <div class="wrap">
    {shead(g["eyebrow"], escape(h))}
    {html}
  </div>
</section>''' for h, html in g["sections"])
    cards = "".join(card("en", p, T["en"]["picks"].get(p, "Program")) for p in g["picks"])
    net = "".join(f'<li><a href="{h}" target="_blank" rel="noopener"><b>{escape(t)}</b></a></li>' for h, t in NET["en"])
    progs = programs.footer_programs("en") + "\n    "
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
{tracking}
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{escape(g["title"])}</title>
<meta name="description" content="{escape(g["desc"])}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#050505">
{verify}
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:locale" content="en_GB">
<meta property="og:site_name" content="STR2G HYROX">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{escape(g["title"])}">
<meta property="og:description" content="{escape(g["desc"])}">
<meta property="og:image" content="{BASE}/img/lada-ria-finish-line.jpg">
<meta name="twitter:card" content="summary_large_image">
{icons}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{fonts}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>{style}</style>
<style>.lp-p a,.lp-list a{{color:var(--gold, #c9a961);text-decoration:underline}}</style>
<style>.sg-box{{border:1px solid var(--line);padding:36px 32px;background:rgba(201,169,80,.06)}}.sg-box h2{{font-size:clamp(38px,5vw,64px);line-height:.95;margin:6px 0 16px}}.sg-box .lead{{max-width:640px}}.st-nav div{{display:flex;flex-wrap:wrap;gap:8px 20px}}.st-nav a{{color:var(--fg);text-decoration:none;font-weight:500}}.st-nav a:hover,.st-nav span{{color:var(--accent)}}</style>
</head>
<body>

<nav class="nav" aria-label="Main">
  <div class="wrap">
    <a class="logo" href="/" aria-label="STR2G HYROX"><img class="mark" src="/favicon.svg?v=2" alt="" width="34" height="34"><b>STR<span class="gold">2</span>G</b></a>
    <div class="navlinks">
      <a class="txt" href="/#programs">{u["programs"]}</a>
      <a class="txt" href="/hyrox-training-plan/">{escape(u["plan_link"])}</a>
      <a class="btn btn-gold" href="#pick">{u["start"]}</a>
    </div>
  </div>
</nav>

<header class="hero lp-hero" id="top">
  <img class="hero-img" src="/img/lada-ria-finish-line.webp" alt="" fetchpriority="high">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">STR2G HYROX</a><span aria-hidden="true">/</span><span>{escape(g["h1"][0])}</span></nav>
    <p class="eyebrow">{escape(g["eyebrow"])}</p>
    <h1 class="display">{escape(g["h1"][0])}<br><span class="gold">{escape(g["h1"][1])}</span></h1>
    <p class="lead">{escape(g["lead"])}</p>
    <div class="cta-row"><a class="btn btn-gold" href="#pick">{u["start"]}</a></div>
  </div>
</header>
{secs}
{(sg_cta() + chr(10) + '<section class="st-links"><div class="wrap">' + station_nav(key) + '</div></section>') if g.get("station") else ""}

<section id="pick">
  <div class="wrap">
    {shead(u["programs"], "Programs that train this")}
    <div class="grid">{cards}</div>
    <p class="lp-note">{escape(u["pay_note"])} <a href="/#programs">{escape(u["all_programs"])} →</a></p>
  </div>
</section>

{faq_html("en", g["faq"])}

<footer>
  <div class="wrap">
    {progs}<nav class="guides" aria-label="Guides"><a href="/hyrox-training-plan/">HYROX training plan</a><a href="/online-hyrox-coach/">Online HYROX coach</a><a href="/programs/">HYROX training programs</a>{nav("en")}</nav>
    <nav class="net" aria-label="STR2G"><p class="net-h">STR2G</p><ul>{net}</ul></nav>
    <div class="links">
      <a href="https://instagram.com/22segge_coach" target="_blank" rel="noopener">@22segge_coach</a>
      <a href="https://instagram.com/riahrusovskaofficial" target="_blank" rel="noopener">@riahrusovskaofficial</a>
      <a href="/privacy/">Privacy policy</a>
      <a href="#" onclick="str2gConsentReset();return false;">Cookies</a>
    </div>
  </div>
</footer>
</body>
</html>
'''
    if g.get("station"):
        from pathlib import Path as _P
        sg = (_P(__file__).resolve().parent / "stationguide.html").read_text(encoding="utf-8").rstrip(chr(10))
        html = html.replace("</body>", sg + chr(10) + "</body>", 1)
    return html


NAV_LABELS = {"hyrox-taper": "HYROX taper", "compromised-running": "Compromised running", "sled-pull": "Sled pull technique", "doubles": "HYROX Doubles", "running": "Run faster in HYROX", "wall-balls": "Wall balls", "skierg": "SkiErg", "sled-push": "Sled push", "burpee-broad-jumps": "Burpee broad jumps", "rowing": "Rowing", "farmers-carry": "Farmers carry", "sandbag-lunges": "Sandbag lunges"}


def nav(lang="en"):
    """Odkazy na zveřejněné průvodce (jen EN) do patičky."""
    if lang != "en":
        return ""
    links = "".join(f'<a href="{g["slug"]}">{escape(NAV_LABELS.get(k, g["slug"]))}</a>' for k, g in GUIDES.items() if not g.get("draft") and not g.get("station"))
    return links + '<a href="/station-guide/">HYROX station guides</a>'


def build(root, parts):
    urls = []
    for key, g in GUIDES.items():
        if g.get("draft"):
            continue
        out = root / g["slug"].strip("/") / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(g, parts, key), encoding="utf-8")
        urls.append(BASE + g["slug"])
    print(f"guides: {len(urls)} written")
    return urls
