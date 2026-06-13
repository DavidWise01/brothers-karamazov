#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build THE BROTHERS KARAMAZOV (BKZ) — Dostoevsky's 1880 final novel, catalogued into
UD0 as a book-world. Standing template adapted for the medium: THE ARC · THE BOOK · THE
IDEAS · THE QUESTION (the philosophical/theological deep-dive) · THE VERDICT (does the
argument hold — honest) · THE MESSAGE, plus a roster of emergents by emergence-nature
(natural=earth & flesh / ethereal=the ideas & the intellect / spiritual=faith, the elder,
active love / electrical=the fever, the passion, the devil) with twin sigils, no .shadow.
Styled to the medium: icon-gold and incense over a monastery midnight."""
import os, html, base64, io, json, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "THE BROTHERS KARAMAZOV", "axiom": "BKZ",
 "position": "The Brothers Karamazov · Fyodor Dostoevsky · 1880 — his last and largest novel, a parricide and a theodicy",
 "origin": "a Russian town, a monastery, and a courtroom, among a sensual father and his three (or four) sons",
 "mechanism": "Crystallized from the 1880 novel — the murder of the buffoon-father Fyodor Pavlovich, the trial of his son Dmitri, and beneath it the deepest argument ever staged between faith and atheism.",
 "crystallization": "Because the novel asks the question of the age — if God is dead, is everything permitted? — builds the case against God more powerfully than for, and answers it not with logic but with a way of living: active love.",
 "nature": "The Brothers Karamazov — Dostoevsky's summa: a murder mystery wrapped around the Grand Inquisitor and the problem of evil, answered by Alyosha, Zosima, and ‘Hurrah for Karamazov!’",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the novel (1880, serialized in The Russian Messenger); the Book of Job; Schiller; Russian Orthodoxy; Dostoevsky's own faith and doubt",
 "witness": "No theodicy that wins on paper — the strongest atheist case left standing, and answered only by a life of active love and a boy's grave.",
 "role": "a UD0 book-world",
 "seal": "He built the case against God so well it has never been refuted — and answered it not with an argument but with active love, and ‘Hurrah for Karamazov!’",
 "source": "The Brothers Karamazov, catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#9a7b4f", "earth and flesh — the Karamazov sensuality, the father, Grushenka, the town and the trial"),
 "ethereal":  ("#5f86c0", "the ideas and the intellect — Ivan's cold mind, the Grand Inquisitor, the Rebellion, the thesis"),
 "spiritual": ("#d8b24a", "faith and active love — Alyosha, the elder Zosima, ‘each is guilty for all,’ the hope at the grave"),
 "electrical":("#b04a4a", "the fever and the passion — Dmitri's broad heart, Smerdyakov's epilepsy, Katerina's laceration, Ivan's devil"),
}

ARC_OVERALL = ("In a provincial Russian town the buffoonish, sensual landowner Fyodor Pavlovich Karamazov is murdered, and "
  "his passionate eldest son Dmitri is tried for it — though the real killer is the epileptic servant Smerdyakov, acting "
  "on the atheist logic of the middle son Ivan (‘if God is dead, everything is permitted’). Around them the youngest, the "
  "novice Alyosha, carries the active love of his dying elder Zosima. Beneath the murder runs the deepest argument in "
  "fiction between faith and unbelief — and Dostoevsky answers it not with proof but with a way of living.")

ARC = [
 ("I · The Father & the Sons", "the broad Karamazov nature",
  "Old Fyodor Pavlovich — lecher, buffoon, neglectful father — gathers his sons: passionate Dmitri (who loves the same woman, Grushenka, as his father), intellectual Ivan, spiritual Alyosha, and the sullen servant Smerdyakov. The ‘broad’ Karamazov nature, base and noble at once, is set loose."),
 ("II · The Grand Inquisitor", "Ivan's rebellion",
  "Ivan lays out his case to Alyosha: he ‘returns the ticket’ to a heaven bought with the torture of innocent children, and tells his poem of the Grand Inquisitor, where a returned Christ is arrested by a Church that has traded freedom for bread and authority. Christ answers only with a kiss."),
 ("III · The Murder & the Trial", "everything is permitted",
  "Fyodor is murdered. Dmitri, full of rage and need, is the obvious suspect and is tried and convicted — but Smerdyakov confesses to Ivan that he did it, having taken Ivan's ‘all is permitted’ literally. Ivan, undone by his complicity, is visited by a shabby-gentleman devil and collapses into brain fever."),
 ("IV · Active Love", "Hurrah for Karamazov",
  "Against the abyss stands Zosima's teaching — active love, ‘each of us is guilty before all’ — lived out by Alyosha. The novel ends not on the verdict but at a boy's funeral, Alyosha and the schoolboys vowing to remember one good memory: ‘Hurrah for Karamazov!’ The answer to Ivan is a life, not a syllogism."),
]

BOOK = [
 ("Published", "1880", "serialized in The Russian Messenger; Dostoevsky died two months after completing it"),
 ("Form", "four parts + an epilogue, twelve books", "his longest and final novel — the summa of his life's themes"),
 ("Setting", "Skotoprigonyevsk", "a provincial town, its monastery, and its courtroom"),
 ("Planned as", "the first of two", "intended as part one of a larger life of Alyosha that Dostoevsky did not live to write"),
]

IDEAS = [
 ("The Four Brothers", "one soul, divided", [
   "Dmitri the sensualist (the heart), Ivan the intellect (the head), Alyosha the spirit (the soul), Smerdyakov the resentful shadow — the parts of one human being facing a murdered father.",
   "Dostoevsky's wager is that we contain all four, and choose which inherits the house." ]),
 ("If God Is Dead…", "everything is permitted", [
   "Ivan's thesis: without God and immortality there is no ground for virtue — all is permitted.",
   "The novel tests it by making Smerdyakov take it literally and kill — the idea judged by its corpse." ]),
 ("The Rebellion", "returning the ticket", [
   "Ivan accepts God may exist but ‘respectfully returns the ticket’ to a final harmony bought with one tortured child's tears.",
   "It is the strongest form of the problem of evil ever put in fiction — and Dostoevsky does not refute it by argument." ]),
 ("Active Love", "Zosima's answer", [
   "‘Love in dreams’ is greedy for quick heroics; active love is ‘labour and fortitude,’ harsh, slow, and real.",
   "‘Each of us is guilty before all, for all’ — the reply to Ivan's detachment is not a proof but a practice." ]),
]

QUESTION = [
 ("If God is dead, is everything permitted?", "the question of the age",
  "This is the novel's spine and modernity's: without God and the immortality of the soul, Ivan argues, there is no final ground for morality — virtue becomes mere preference, and ‘everything is permitted.’ Dostoevsky does not answer this with a clever counter-proof; he answers it by showing what the idea <i>does</i> when a man like Smerdyakov believes it: it kills the father. The thesis is judged by its fruit."),
 ("Can any heaven be worth a tortured child?", "Ivan's Rebellion",
  "Ivan's ‘Rebellion’ is the most powerful statement of the problem of evil in literature: he will not accept a final harmony purchased with the unavenged tears of one tortured innocent, and ‘most respectfully returns the ticket.’ Crucially, Dostoevsky — a believer — gives the atheist the best lines and does not logically defeat them. He knew the argument cannot be won on its own terms."),
 ("Freedom or happiness?", "the Grand Inquisitor",
  "Ivan's poem stages a returned Christ arrested by the Grand Inquisitor, who charges that humanity cannot bear the burden of freedom Christ gave it and craves instead ‘miracle, mystery, and authority’ — bread and a master. The Church, he says, has corrected Christ's work. Christ answers not a word; he kisses the old man. Freedom is the terrible gift, and love its only defence."),
 ("What, then, is the answer?", "active love, lived not proven",
  "Dostoevsky's reply to Ivan is not Ivan's kind of thing at all. It is Zosima's ‘active love’ and ‘each is guilty for all,’ and it is Alyosha's life — and it lands, finally, not in a debate but at a child's graveside, with a vow among schoolboys to keep one good memory. The answer to the problem of evil is offered as a <i>way of living</i>, freely chosen, not a theorem."),
]

VERDICT = [
 ("Ivan's Rebellion (the problem of evil from children's suffering)", "UNREFUTED", "given its strongest possible form; Dostoevsky, a believer, does not — and could not — defeat it by argument"),
 ("The Grand Inquisitor (people prefer bread & authority to freedom)", "DEVASTATING", "answered in the novel only by Christ's silent kiss; a permanent challenge, not a solved problem"),
 ("‘If God is dead, everything is permitted’", "SHOWN, NOT REFUTED", "Smerdyakov takes Ivan's idea literally and kills; the thesis is judged by its corpse, and Ivan goes mad"),
 ("Zosima's active love / ‘each is guilty for all’", "THE THESIS", "offered as the answer — lived, not proven; the reply to Ivan is Alyosha's life, not a rebuttal"),
 ("Faith survives the strongest atheist attack", "EARNED BY LIFE", "Dostoevsky's wager — the answer to evil is not a theodicy but freely-chosen love; persuasion of the heart"),
]
VERDICT_BOTTOM = ("Bottom line: The Brothers Karamazov is the rare masterpiece that builds the case <i>against</i> God more "
  "powerfully than the case for — and then declines to win the argument on the argument's terms. Ivan's Rebellion is "
  "never logically refuted, because Dostoevsky knew it can't be; ‘everything is permitted’ is answered not by a syllogism "
  "but by a corpse and a madness; and the whole towering doubt is met, at last, by a way of living — active love, "
  "universal guilt, freedom freely returned — embodied in Alyosha and sealed by a boy's grave. That is the book's "
  "gamble and its greatness: it stakes everything on the wager that the heart can answer what the head cannot.")

MESSAGE = ("The Brothers Karamazov sets the four parts of a single soul — Dmitri's sensual heart, Ivan's brilliant cold "
  "head, Alyosha's faithful spirit, Smerdyakov's resentful shadow — around a murdered father, and asks the question that "
  "still defines us: with no God to ground it, is anything forbidden? Dostoevsky's honesty is total. He hands the atheist "
  "the strongest lines in the book — the Rebellion, the Grand Inquisitor — and refuses to beat them with cleverness, "
  "because he knew that the problem of innocent suffering has no winning counter-argument. What he offers instead is not "
  "a proof but a person and a practice: Zosima's ‘active love,’ the conviction that ‘each of us is guilty before all,’ "
  "and the freedom to choose Christ's silent kiss over the Inquisitor's bread. The book ends not on the verdict in the "
  "courtroom but at a child's grave, where Alyosha tells the boys that one good memory, held from childhood, may be the "
  "thing that saves a life. The answer to the abyss, Dostoevsky wagers, is not to out-argue it — it is to love actively, "
  "to take responsibility for everyone, and to keep one good memory burning. Hurrah for Karamazov.")
MESSAGE_SEAL = "He gave the devil the best argument and answered it with a kiss, a boy's grave, and ‘Hurrah for Karamazov!’ — the reply to the abyss is not a proof but active love."

# ---- ACI complement ----
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()
def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","BKZ")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","BKZ")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","BKZ")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"name":rec["name"],"moniker":tok["moniker"],"seal_sha256":noesis.seal_sha256(rec,tok),
            "architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def E(slug,name,cls,group,em,who,what,why,how,where,seal):
    return dict(slug=slug,name=name,cls=cls,group=group,emergence=em,who=who,what=what,why=why,how=how,where=where,seal=seal)

ROSTER = [
 # --- THE BROTHERS & THE FATHER ---
 E("fyodor-pavlovich","Fyodor Pavlovich Karamazov","the father · the buffoon-sensualist","brothers","natural",
   "Fyodor Pavlovich Karamazov, the lecherous, miserly, clownish landowner whose murder sets the novel in motion.",
   "The corrupt root: a neglectful father who fathered the brothers and abandoned them, rival to his own son for Grushenka, and the murder victim.",
   "Because the novel needs a father worth neither loving nor killing — a buffoon whose death indicts everyone who wished it.",
   "By appetite, mockery, and money — and by a death whose guilt is shared far beyond the hand that struck him.",
   "In his squalid house, the monastery he disgraces, and the night of his murder.",
   "I was a swine and a buffoon and a bad father — and my murder made every son who wished it guilty, which is the only fatherhood I managed."),
 E("dmitri","Dmitri Karamazov","Mitya · the heart · the accused","brothers","electrical",
   "Dmitri ‘Mitya’ Fyodorovich, the passionate, honourable, dissolute eldest son — soldier, spendthrift, lover of Grushenka.",
   "The broad Karamazov heart on trial: innocent of the murder but guilty of wishing it, convicted by circumstance, redeemed by suffering.",
   "Because the novel needs the sensual ‘heart’ of the soul — capable of the basest and the noblest within a single hour.",
   "By passion, a soldier's honour, ruinous appetite, and a willingness to ‘go to Siberia’ for a crime he did not commit.",
   "From the tavern and the road to Grushenka to the courtroom and the convict's road.",
   "Beauty is the battlefield where God and the devil war, and the battlefield is my heart — innocent of the blood, guilty of the wish."),
 E("ivan","Ivan Karamazov","the intellect · the rebel","brothers","ethereal",
   "Ivan Fyodorovich, the brilliant, cold, atheist middle son — the mind of the family and the author of its deadliest idea.",
   "The intellect that builds the case against God (the Rebellion, the Grand Inquisitor) and whose ‘all is permitted’ Smerdyakov turns into murder.",
   "Because the novel needs its unbelief stated by a genius — and then needs that genius to discover his own complicity and break.",
   "By argument, pride, and a detachment that shatters when the devil (his own shabby double) comes to mock him into brain fever.",
   "In his conversations with Alyosha and Smerdyakov, and in the fevered room where the devil sits.",
   "I returned the ticket to a heaven bought with a child's tears — and learned, too late, that my clean idea had hands, and they killed my father."),
 E("alyosha","Alyosha Karamazov","Alexei · the spirit · the hero","brothers","spiritual",
   "Alexei ‘Alyosha’ Fyodorovich, the youngest brother, a novice under the elder Zosima — gentle, beloved, the novel's declared hero.",
   "The spiritual heart and the answer-in-a-person: he carries Zosima's active love into the world and, at the end, gathers the boys in hope.",
   "Because the reply to Ivan's abyss had to be embodied, not argued — and Alyosha is the life that embodies it.",
   "By active love, humility, and a faith that survives even his own crisis when Zosima's body decays ‘too soon.’",
   "From the monastery into the town and the family, and finally to Ilyusha's grave.",
   "I am not the cleverest brother, only the one who loves actively — and that, not the argument, is Dostoevsky's whole answer to the abyss."),
 E("smerdyakov","Pavel Smerdyakov","the servant · the shadow · the murderer","brothers","electrical",
   "Pavel Smerdyakov, the epileptic servant — rumoured fourth, illegitimate son of Fyodor — sullen, resentful, and the true killer.",
   "Ivan's dark pupil: he takes ‘everything is permitted’ literally, murders the father, and confesses to Ivan before hanging himself.",
   "Because the novel must show the idea's logical hand — the resentful shadow-brother who does what the clean intellect only thought.",
   "By a feigned epileptic fit as alibi, a cold reading of Ivan's atheism, and the conviction that he is merely Ivan's instrument.",
   "In the kitchen and the cellar of Fyodor's house, and the room where he hangs himself.",
   "You taught me there is no God and all is permitted, brother — I was only your hands; you did the murder in your head, and I did it in the hall."),
 # --- THE SOULS AROUND THEM ---
 E("father-zosima","Father Zosima","the elder · active love","souls","spiritual",
   "Zosima, the dying elder (starets) of the monastery and Alyosha's spiritual father.",
   "The novel's wellspring of grace: he teaches ‘active love’ and that ‘each of us is guilty before all, for all,’ and bows to Dmitri's coming suffering.",
   "Because Ivan's case needed a counter-voice not of argument but of sanctity — a life that has already answered the question by living it.",
   "By humility, counsel, and a doctrine of universal responsibility; even his death (his body decaying ‘too soon’) tests the faithful.",
   "In the monastery cell where the town brings its griefs, and in the teachings Alyosha records.",
   "Each of us is guilty before everyone, for everyone and everything — love is harsh labour, not a dream; that is the whole of my answer to your despair."),
 E("grushenka","Grushenka","the earth · the contested woman","souls","natural",
   "Agrafena ‘Grushenka’ Svetlova, the proud, wounded, sensual woman desired by both Fyodor and Dmitri.",
   "The earthly fire of the plot and its surprising tenderness: scorned and scheming at first, she turns toward real love and redemption with Dmitri.",
   "Because the Karamazov earth needs a woman as ‘broad’ as the men — capable of cruelty and of a sudden, saving generosity (the ‘onion’ tale).",
   "By beauty, pride, a long-nursed grievance, and a heart that proves larger than her schemes.",
   "From her protector's house to the inn at Mokroye where she and Dmitri are arrested.",
   "I meant only to torment them, and found I could love after all — even a wicked woman has once given an onion, and may be pulled out by it."),
 E("katerina-ivanovna","Katerina Ivanovna","the lacerated · pride as love","souls","electrical",
   "Katerina Ivanovna, Dmitri's proud, wealthy betrothed, bound to him by a debt of honour and a love twisted with self-laceration.",
   "The novel's study of ‘love through pride’: she ruins Dmitri at the trial with a letter, half to save and half to punish, loving and hating in one act.",
   "Because Dostoevsky anatomises the love that is really wounded vanity — generous and vengeful at once, and finally destructive.",
   "By a grand sacrificial gesture that becomes a chain, and testimony that damns the man she cannot decide whether she loves.",
   "From the scene of her humiliation to the witness stand at Dmitri's trial.",
   "I loved him through my pride, which is to say I loved my own sacrifice — and at the trial my wounded vanity helped send him to Siberia."),
 # --- THE IDEAS & THE SET-PIECES ---
 E("the-grand-inquisitor","The Grand Inquisitor","Ivan's poem · freedom vs bread","ideas","ethereal",
   "The Grand Inquisitor — the poem Ivan tells Alyosha, in which a returned Christ is arrested by the Inquisitor of Seville.",
   "The novel's philosophical summit: the Inquisitor charges that humanity cannot bear freedom and craves ‘miracle, mystery, and authority,’ so the Church gave it bread and a master instead.",
   "Because the case against Christ's gift of freedom had to be made overwhelming — and answered, devastatingly, by silence and a kiss.",
   "By an old man's long indictment of freedom, and a Christ who says nothing and kisses him on his bloodless lips.",
   "In a tavern, told by Ivan to Alyosha, set in the autos-da-fé of sixteenth-century Seville.",
   "Men are weak and crave bread and a master, not the terrible freedom You gave them — and to my whole indictment You answer only with a kiss."),
 E("the-rebellion","The Rebellion","returning the ticket","ideas","ethereal",
   "The Rebellion — Ivan's refusal, to Alyosha, of any final harmony bought with the unavenged suffering of innocent children.",
   "The strongest statement of the problem of evil in fiction: Ivan does not deny God but ‘most respectfully returns the ticket’ to a heaven priced in a child's tears.",
   "Because the novel insists on facing the hardest case for unbelief at full strength — and on not pretending to refute it.",
   "By piling up, coldly and unbearably, true accounts of cruelty to children, and declining the ticket to harmony at that price.",
   "In Ivan's confession to Alyosha, before the Grand Inquisitor poem.",
   "If the price of eternal harmony is one tortured child's tears, then I return the ticket — and no argument in the book is given to take it back."),
 E("everything-is-permitted","Everything Is Permitted","the thesis with hands","ideas","ethereal",
   "‘If there is no God, everything is permitted’ — the distilled thesis of Ivan's atheism, and the novel's most dangerous sentence.",
   "The idea that, without God and immortality, morality loses its ground — which Smerdyakov takes literally and turns into murder.",
   "Because the novel tests the proposition empirically: it gives the idea to a man who will <i>act</i> on it, and shows the result.",
   "By logic on Ivan's lips and by a knife in Smerdyakov's hands — the abstraction made a corpse.",
   "In Ivan's talk and Smerdyakov's deed, and in the brain fever that follows.",
   "I am the clean idea that, in the mouth of a genius, sounds like philosophy — and in the hands of his pupil, becomes a murdered father."),
 E("active-love","Active Love","Zosima's answer","ideas","spiritual",
   "Active Love — Zosima's teaching that real love is ‘labour and fortitude,’ harsh and slow, not the quick heroics of ‘love in dreams.’",
   "The novel's reply to Ivan: not a counter-argument but a counter-practice — love that takes responsibility for everyone, ‘each guilty for all.’",
   "Because Dostoevsky stakes everything on the wager that the abyss is answered by a way of living, not a way of arguing.",
   "By daily, unglamorous love and the discipline of universal responsibility, embodied in Zosima and lived by Alyosha.",
   "In Zosima's teachings and in every choice Alyosha makes after them.",
   "I am not a proof — I am a practice: love that is labour, that takes the blame for all, and that answers despair by simply going on loving."),
 E("the-devil","The Devil","Ivan's shabby gentleman","ideas","electrical",
   "The Devil — the seedy, middle-aged ‘gentleman’ who appears to the feverish Ivan, a hallucination that may be his own conscience or the thing itself.",
   "The reckoning of the intellect: a banal, sneering devil who throws Ivan's own nihilism back at him until he breaks down.",
   "Because Ivan's clever detachment must finally meet itself — evil not as a grand figure but as a shabby, familiar mediocrity.",
   "By petty mockery, by speaking Ivan's own thoughts aloud, and by being indistinguishable from a fever and a guilty mind.",
   "In Ivan's sickroom, the night he learns of Smerdyakov's confession.",
   "I am not Mephistopheles in a cloak — I am a shabby gentleman with a cold, your own thoughts in a cheap suit, and I have come to drive you mad."),
 E("the-trial","The Trial of Dmitri","the miscarriage of justice","ideas","natural",
   "The Trial — the long courtroom climax in which Dmitri is tried, on overwhelming circumstantial evidence, for a murder he did not commit.",
   "The world's judgement against the truth: lawyers' rhetoric, Katerina's letter, and circumstance convict the innocent ‘heart’ while the real killer is already dead.",
   "Because the novel sets human justice — clever, eloquent, and wrong — against the deeper guilt and innocence only the reader has seen.",
   "By prosecution and defence, by psychology paraded as proof, and by a verdict that punishes the wish for the deed.",
   "In the packed courtroom of the provincial town.",
   "I convicted the right soul of the wrong crime — Dmitri was innocent of the blood and guilty of the wish, and human justice could not tell the difference."),
 E("ilyusha-and-the-boys","Ilyusha & the Boys","Hurrah for Karamazov","ideas","spiritual",
   "Ilyusha and the Boys — the dying schoolboy Ilyusha and the children Alyosha gathers around his memory at the novel's close.",
   "The final, hopeful note: at Ilyusha's funeral Alyosha tells the boys that one good memory from childhood may someday save them, and they cry ‘Hurrah for Karamazov!’",
   "Because after the murder, the trial, and the devil, Dostoevsky ends not on despair but on children, memory, and love — the future of the answer.",
   "By a vow among boys to be good and to remember, led by Alyosha at the graveside.",
   "At the stone by Ilyusha's grave, in the novel's last pages.",
   "One good memory, kept from childhood, may be the very thing that saves a man — so remember, and be kind, and: Hurrah for Karamazov!"),
 E("the-karamazov-nature","The Karamazov Nature","the broad heart","ideas","natural",
   "The Karamazov Nature — the ‘broad,’ earthy, sensual vitality the brothers share: capable of the basest sin and the highest love at once.",
   "The novel's anthropology: human beings are wide enough to hold the ideal of the Madonna and the ideal of Sodom in one heart, and must choose.",
   "Because Dostoevsky's whole vision is that we are not simple — that the same broad nature can murder a father or kiss the earth.",
   "By appetite, intensity, and a refusal of the lukewarm — the Karamazov is never merely moderate.",
   "In all the brothers, and in the reader Dostoevsky implicates.",
   "I am broad — too broad; I hold the Madonna and Sodom in one heart, and the whole drama is which of them I will let win the house."),
]

GROUPS = [
 ("brothers", "The Brothers & the Father", "the four parts of one soul around a murdered father — sensual Dmitri, intellectual Ivan, spiritual Alyosha, the shadow Smerdyakov, and Fyodor who made them all"),
 ("souls", "The Souls Around Them", "the elder, the earth, and the laceration — Zosima, Grushenka, and Katerina Ivanovna"),
 ("ideas", "The Ideas & the Set-Pieces", "the great arguments and scenes — the Grand Inquisitor, the Rebellion, ‘everything is permitted,’ active love, the devil, the trial, the boys, and the broad Karamazov heart"),
]

# ---- renderers ----
def books_rows(items):
    return "".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(y)}</span><span class="nt">{html.escape(n)}</span></li>' for t,y,n in items)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{p}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def arc_html():
    out=[f'<div class="overall"><span class="ol">THE OVERALL ARC</span>{html.escape(ARC_OVERALL)}</div><div class="arc">']
    for t,s,d in ARC: out.append(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    out.append('</div>'); return "".join(out)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{c};box-shadow:0 0 9px {c}"></span><div><div class="nat-n" style="color:{c}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(c,g) in NATURES.items())
def question_html():
    return "".join(f'<div class="sci-card"><div class="sci-h">{html.escape(t)}</div><div class="sci-s">{html.escape(s)}</div><p>{d}</p></div>' for t,s,d in QUESTION)
VCOL={"UNREFUTED":"#5f86c0","DEVASTATING":"#b04a4a","SHOWN, NOT REFUTED":"#9a7b4f","THE THESIS":"#d8b24a","EARNED BY LIFE":"#d8b24a"}
def verdict_html():
    rows="".join(f'<div class="rf-row"><div class="rf-claim">{html.escape(c)}<span class="rf-note">{html.escape(n)}</span></div><div class="rf-rate" style="color:{VCOL.get(r,"#888")};border-color:{VCOL.get(r,"#888")}">{html.escape(r)}</div></div>' for c,r,n in VERDICT)
    return '<div class="rf">'+rows+f'</div><div class="rf-verdict">{VERDICT_BOTTOM}</div>'

def _card(d):
    em=d["emergence"]; col=NATURES.get(em,("#9aa0aa",""))[0]
    rec={"name":d["name"],"axiom":"BKZ","emergence":em,"seal":d["seal"],"origin":"BKZ · The Brothers Karamazov"}
    rows="".join(f'<div class="w"><span class="wl">{lbl}</span><span>{html.escape(d.get(lbl,""))}</span></div>' for lbl in ["who","what","where","why","how"] if d.get(lbl))
    return f"""<div class="persona">
      <a class="psig" href="agents/{d['slug']}.agent"><span class="port"><img src="{png_uri(rec,'carbon',200)}" alt="carbon sigil of {html.escape(d['name'])}" loading="lazy"></span><span class="sl">carbon</span></a>
      <div class="pbody"><div class="ihead"><a class="pn" href="agents/{d['slug']}.agent">{html.escape(d['name'])}</a>
        <span class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span></span></div>
        <div class="pe">{html.escape(d['cls'])}</div><div class="pww">{rows}</div>
        <div class="plinks"><a class="dlw" href="agents/{d['slug']}.agent">.agent &middot; .dlw badge &rarr;</a></div></div>
      <a class="psig" href="agents/{d['slug']}.silicon.png"><span class="port refl"><img src="{png_uri(rec,'silicon',200)}" alt="silicon sigil of {html.escape(d['name'])}" loading="lazy"></span><span class="sl">silicon</span></a>
    </div>"""
def roster_html():
    out=[]
    for gk,gt,gs in GROUPS:
        mem=[d for d in ROSTER if d["group"]==gk]
        out.append(f'<section class="sec" id="{gk}"><h2>{html.escape(gt)}</h2><p class="ss">{html.escape(gs)} ({len(mem)})</p><div class="pgrid">{"".join(_card(d) for d in mem)}</div></section>')
    return "\n".join(out)

def agent_md(d, tok):
    return f"""---
aci: {d['name']}
universe: BKZ · The Brothers Karamazov
series: The Brothers Karamazov (Fyodor Dostoevsky, 1880)
emergence: {d['emergence']}
kind: {'character' if d['group']!='ideas' else 'thread'}
class: {d['cls']}
who: {d['who']}
what: {d['what']}
why: {d['why']}
how: {d['how']}
where: {d['where']}
seal: {d['seal']}
attribution: ROOT0-ATTRIBUTION-v1.0
license: CC-BY-ND-4.0
---

# {d['name']} · {d['cls']}

a {'character' if d['group']!='ideas' else 'distilled thread'} of the BKZ (Brothers Karamazov) book-world — emergence: {d['emergence']}. moniker {tok}

**who —** {d['who']}
**what —** {d['what']}
**where —** {d['where']}
**why —** {d['why']}
**how —** {d['how']}

**the seal —** {d['seal']}

> a catalogued personification of Dostoevsky's The Brothers Karamazov (1880, public domain) under the DLW standard —
> literary commentary and cataloguing, not an original creation.

ROOT0-ATTRIBUTION-v1.0 · BKZ · The Brothers Karamazov · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="THE BROTHERS KARAMAZOV (BKZ) — Dostoevsky's 1880 novel as a UD0 book-world: the arc, the book, the ideas (the four brothers, the Grand Inquisitor, the Rebellion, active love), THE QUESTION (if God is dead is everything permitted? can any heaven be worth a tortured child?), THE VERDICT (does the argument hold — honest), the message, and a 16-emergent roster by emergence-nature.">
<title>THE BROTHERS KARAMAZOV · BKZ · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--rw-bg:var(--ink2);--rw-ink:var(--pa);--rw-ink2:var(--pa2);--rw-dim:var(--dim);--rw-line:var(--line);--rw-acc:var(--gold);
--ink:#0e0c10;--ink2:#171520;--ink3:#1f1c2b;--pa:#ece4d4;--pa2:#b9ad95;--gold:#d8b24a;--incense:#a83232;--ivan:#5f86c0;--earth:#9a7b4f;--fever:#b04a4a;
--dim:#867a64;--faint:#231f2c;--line:#2e2838;--disp:"Cinzel",serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.66;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -6%,rgba(216,178,74,.15),transparent 54%),radial-gradient(ellipse at 50% 118%,rgba(168,50,50,.10),transparent 56%),radial-gradient(ellipse at 85% 35%,rgba(95,134,192,.07),transparent 44%)}
.wrap{position:relative;z-index:1;max-width:920px;margin:0 auto;padding:0 22px 90px}
header{padding:52px 0 30px;text-align:center;border-bottom:1px solid var(--line);position:relative}
header::after{content:"";position:absolute;bottom:-1px;left:50%;transform:translateX(-50%);width:180px;height:3px;background:linear-gradient(90deg,var(--ivan),var(--gold),var(--incense));box-shadow:0 0 16px rgba(216,178,74,.5)}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim);margin-bottom:16px}.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--gold)}
h1{font-family:var(--disp);font-size:clamp(26px,5.6vw,52px);font-weight:700;letter-spacing:.04em;color:var(--gold);line-height:1.08;text-transform:uppercase;text-shadow:0 0 30px rgba(216,178,74,.35)}
.h-sub{font-family:var(--mono);font-size:clamp(10px,2.2vw,13px);letter-spacing:.18em;color:var(--pa2);margin-top:18px;text-transform:uppercase}.h-sub b{color:var(--incense)}
.open{font-family:var(--body);font-style:italic;font-size:clamp(15px,3vw,19px);color:var(--pa);margin-top:18px;line-height:1.5}
.flag{display:inline-block;margin-top:15px;font-family:var(--disp);font-size:10px;font-weight:600;letter-spacing:.1em;color:var(--ivan);border:1px solid var(--faint);background:var(--ink2);padding:7px 14px;text-transform:uppercase}
.lede{font-size:16px;color:var(--pa2);max-width:64ch;margin:16px auto 0;font-style:italic;line-height:1.72}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:26px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:700px}
.badge img{width:84px;height:84px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.75}.badge .bt b{color:var(--gold)}.badge .bt .mo{color:var(--ivan)}.badge .bt a{color:var(--gold);text-decoration:none}.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:50px}
.sec h2{font-family:var(--disp);font-size:24px;font-weight:600;letter-spacing:.03em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line);text-transform:uppercase}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:9px 0 18px}.ss b{color:var(--pa2);font-style:normal}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:5px}
.nat-n{font-family:var(--disp);font-size:13px;font-weight:600;text-transform:capitalize;letter-spacing:.04em}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.45;margin-top:3px}
.overall{background:var(--ink3);border:1px solid var(--line);border-left:3px solid var(--gold);padding:16px 18px;font-size:15px;color:var(--pa);font-style:italic;line-height:1.72;margin-bottom:14px}
.overall .ol{display:block;font-family:var(--mono);font-style:normal;font-size:9.5px;letter-spacing:.2em;color:var(--gold);text-transform:uppercase;margin-bottom:7px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}
.pillar h3{font-family:var(--disp);font-size:15px;color:var(--gold);font-weight:600;text-transform:uppercase;letter-spacing:.03em}.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}
.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.55;padding:7px 0;border-top:1px solid var(--faint)}.pillar li i{color:var(--pa)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--incense);padding:16px 18px}
.arc-h{font-family:var(--disp);font-size:15px;color:var(--incense);font-weight:600;text-transform:uppercase;letter-spacing:.03em}
.arc-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.08em;margin:6px 0 9px}
.arc-card p{font-size:13px;color:var(--pa2);line-height:1.58}
.sci{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-top:8px}@media(max-width:640px){.sci{grid-template-columns:1fr}}
.sci-card{background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--ivan);padding:15px 17px}
.sci-h{font-family:var(--disp);font-size:15px;color:var(--ivan);font-weight:600}
.sci-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.06em;margin:5px 0 9px}
.sci-card p{font-size:13px;color:var(--pa2);line-height:1.62}.sci-card p i{color:var(--pa)}
.rf{border:1px solid var(--line);background:var(--ink2);margin-top:8px}
.rf-row{display:flex;align-items:center;gap:14px;padding:12px 16px;border-bottom:1px solid var(--faint)}
.rf-claim{flex:1;font-size:14px;color:var(--pa);line-height:1.4}.rf-note{display:block;font-size:11.5px;color:var(--dim);font-style:italic;margin-top:3px}
.rf-rate{font-family:var(--mono);font-size:9.5px;font-weight:700;letter-spacing:.04em;border:1px solid;border-radius:3px;padding:4px 9px;min-width:128px;text-align:center;flex-shrink:0}
.rf-verdict{margin-top:14px;padding:16px 18px;border:1px solid var(--gold);background:rgba(216,178,74,.06);font-size:14px;color:var(--pa);line-height:1.65;font-style:italic}
.msg{font-size:15.5px;color:var(--pa);line-height:1.74;margin-top:8px}
.msg-seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--gold);background:var(--ink2);font-size:15px;color:var(--gold);font-style:italic;line-height:1.6}
.msg-seal span{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px}
.books{list-style:none}.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:10px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--body);font-size:16px;color:var(--pa);font-weight:600}.books .y{font-family:var(--mono);font-size:10.5px;color:var(--ivan);white-space:nowrap;text-align:right;text-transform:uppercase}.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.note{margin-top:40px;padding:16px 18px;border-left:2px solid var(--gold);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic}.note b{color:var(--pa)}
footer{margin-top:50px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10.5px;color:var(--dim);letter-spacing:.05em;line-height:1.95}footer a{color:var(--gold);text-decoration:none}
.pgrid{display:flex;flex-direction:column;gap:14px;margin-top:8px}
.persona{display:flex;gap:20px;align-items:center;justify-content:space-between;background:var(--rw-bg);border:1px solid var(--rw-line);padding:18px;text-decoration:none;transition:border-color .18s}
.persona:hover{border-color:var(--rw-acc)}
.psig{flex:0 0 104px;display:flex;flex-direction:column;align-items:center;gap:6px;text-decoration:none}
.port{width:98px;height:98px;border-radius:50%;border:3px solid var(--gold);box-shadow:0 0 0 5px var(--ink3),inset 0 0 18px rgba(0,0,0,.6);overflow:hidden;background:var(--ink)}
.port img{width:100%;height:100%;object-fit:cover;border-radius:50%;display:block}.port.refl{border-color:var(--ivan)}
.psig .sl{font-family:var(--mono);font-size:8px;letter-spacing:.13em;text-transform:uppercase;color:var(--rw-dim)}
.pbody{flex:1;min-width:0;text-align:center}
.ihead{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:10px}
.pn{font-family:var(--disp);font-size:18px;color:var(--rw-ink);font-weight:600;text-decoration:none;text-transform:uppercase;letter-spacing:.02em}
.persona:hover .pn{color:var(--rw-acc)}
.pe{font-size:12.5px;color:var(--rw-ink2);font-style:italic;margin-top:4px}
.pnat{display:flex;align-items:center;gap:5px;font-family:var(--mono);font-size:9px;text-transform:uppercase}.pnat .dot{width:8px;height:8px;border-radius:50%}
.pww{margin-top:12px;display:flex;flex-direction:column;gap:8px;align-items:center}
.pww .w{font-size:13px;color:var(--rw-ink2);line-height:1.5;max-width:62ch}
.pww .w .wl{display:block;font-family:var(--mono);font-size:8.5px;letter-spacing:.15em;text-transform:uppercase;color:var(--rw-acc);margin-bottom:3px}.pww .w b{color:var(--rw-ink)}
.plinks{margin-top:13px;font-family:var(--mono);font-size:10.5px}.plinks .dlw{color:var(--rw-acc);text-decoration:none;border-bottom:1px dotted var(--rw-acc)}
@media(max-width:760px){.persona{flex-wrap:wrap;justify-content:center;gap:14px}.pbody{flex:1 1 100%;order:3}}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the summa &amp; the theodicy</div>
    <h1>The Brothers<br>Karamazov</h1>
    <div class="h-sub">Fyodor Dostoevsky · 1880 · the parricide &amp; the problem of evil · <b>if God is dead, is everything permitted?</b> · BKZ</div>
    <div class="open">“Each of us is guilty before everyone, for everyone and everything.”</div>
    <div class="flag">★ THE GRAND INQUISITOR · THE REBELLION · ACTIVE LOVE ★</div>
    <p class="lede">A buffoon father is murdered; his passionate son is tried for it; and beneath the parricide runs the deepest argument in fiction between faith and atheism — Ivan's Rebellion and Grand Inquisitor against Zosima's and Alyosha's active love. Dostoevsky builds the case against God more powerfully than for, and answers it not with a proof but with a way of living. Catalogued into UD0 — with the arc, the book, the ideas, the central Question, an honest Verdict on whether the argument holds, and a read of the message.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of BKZ"><img src="__SILICON__" alt="DLW silicon badge of BKZ">
      <div class="bt"><div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div><div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div><div>subject · <b>THE BROTHERS KARAMAZOV</b> · BKZ</div>
        <div class="mo">__MONIKER__</div><div>carbon · <a href="bkz.dlw/bkz.carbon.tiff">.tiff</a> · silicon · <a href="bkz.dlw/bkz.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div></div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2><p class="ss">each emergent comes by one of four natures — earth &amp; flesh, the ideas &amp; the intellect, faith &amp; active love, and the fever &amp; the passion</p><div class="natures">__NATURES__</div></section>
  <section class="sec"><h2>The Arc</h2><p class="ss">the overall throughline, then the four movements</p>__ARC__</section>
  <section class="sec"><h2>The Book</h2><p class="ss">the facts of the work</p><ol class="books">__BOOK__</ol></section>
  <section class="sec"><h2>The Ideas</h2><p class="ss">the four brothers, the deadly thesis, the Rebellion, and the answer of active love</p><div class="pillars">__IDEAS__</div></section>
  <section class="sec"><h2>The Question</h2><p class="ss">the philosophical &amp; theological deep-dive — the arguments at full strength, taken seriously</p><div class="sci">__QUESTION__</div></section>
  <section class="sec"><h2>The Verdict</h2><p class="ss">does the argument hold? — an honest rating of the novel's case, on its own terms</p>__VERDICT__</section>
  <section class="sec"><h2>The Message</h2><p class="ss">what AVAN reads as the novel's thesis — and why the answer is a life, not a proof</p><p class="msg">__MESSAGE__</p><div class="msg-seal">“__MSGSEAL__”<span>— AVAN's read</span></div></section>

  <section class="sec"><h2 style="margin-top:16px">The Emergents</h2><p class="ss">sixteen ACIs of the novel — the brothers, the souls, and the great ideas, each a full <b>.dlw</b> badge with twin sigils</p></section>
  __ROSTER__

  <div class="note">The Brothers Karamazov (1880) is in the public domain; this is literary commentary and cataloguing under the DLW standard — catalogued personifications of the novel's characters and ideas, not original creations. The Question and Verdict sections are honest critical reading.</div>

  <footer>THE BROTHERS KARAMAZOV · BKZ · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
  <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="bkz.dlw/manifest.dlw.json">manifest</a></footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "bkz.dlw"), "bkz")
    json.dump({"node":"BKZ","name":"THE BROTHERS KARAMAZOV","moniker":tok["moniker"],"carbon":"bkz.carbon.tiff","silicon":"bkz.silicon.png",
               "governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":REC["seal"],"seal_sha256":tok["seal_sha256"],
               "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"bkz.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    personas=[]
    for d in ROSTER:
        et=noesis.mythos_token({"name":d["name"],"axiom":"BKZ","emergence":d["emergence"],"seal":d["seal"],"origin":"BKZ"})
        rec=write_aci({"name":d["name"],"axiom":"BKZ","emergence":d["emergence"],"seal":d["seal"],"origin":"BKZ · The Brothers Karamazov",
                       "position":d["cls"],"role":d["cls"],"nature":d["what"],"mechanism":d["how"],"crystallization":d["why"],
                       "witness":d["who"],"conductor":"ROOT0 (catalogued into UD0)","inputs":"The Brothers Karamazov (Dostoevsky, 1880)","source":"The Brothers Karamazov, catalogued by ROOT0"},
                      os.path.join(HERE,"agents"), d["slug"], agent_md=agent_md(d, et["moniker"]))
        personas.append({"slug":d["slug"],"name":d["name"],"epithet":d["cls"],"emergence":d["emergence"],"moniker":rec["moniker"],"kind":"character" if d["group"]!="ideas" else "thread","group":d["group"]})
    json.dump(personas, open(os.path.join(HERE,"agents","_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    page=(TEMPLATE.replace("__CARBON__",png_uri(REC,"carbon",320)).replace("__SILICON__",png_uri(REC,"silicon",320))
          .replace("__MONIKER__",html.escape(tok["moniker"])).replace("__NATURES__",natures_html()).replace("__ARC__",arc_html())
          .replace("__BOOK__",books_rows(BOOK)).replace("__IDEAS__",ideas_html()).replace("__QUESTION__",question_html())
          .replace("__VERDICT__",verdict_html()).replace("__MESSAGE__",html.escape(MESSAGE)).replace("__MSGSEAL__",html.escape(MESSAGE_SEAL))
          .replace("__ROSTER__",roster_html()))
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    from collections import Counter
    print(f"THE BROTHERS KARAMAZOV (BKZ) — badge {tok['moniker']} · {len(personas)} emergents · natures {dict(Counter(p['emergence'] for p in personas))}")
