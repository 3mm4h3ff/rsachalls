# -*- coding: utf-8 -*-
import binascii
import gmpy2

p = 178303473786440649576050320052579710545803909989892629205383717584926708902831849776048732760539010762697595927799936684517659903020504217647033543451220035557888294087176752636393814444659024479926738965907728305885121533795396510942655193238103461141541226710219917283161689995423704003910208566347008192777
q = 177704742022668281567275022430710622044625631943464584783356816417678451913814558943536631037762187048467689046234818780661519865062083219860810518179422654892088803969419990517131405785258854547965943290573901682173757368660288706014607783317852866568116668579647747712013357379386510690231133643640946552973
dp = 1773866135293945458650606659967376768479853354798205505926578632915333539903357890260215965940940766548344180309223167345247940198199013532903029896549971209908039241113252707919629629337895905532939161172648104970277846713071982622558420220505110955098415853869774113380554829745277553298891557215897116769
dq = 16347740812894503403712423672654444669530920472208797803665993960391586227449959196645900003458629868855939351202369996011540095922292746578891719396733741037038671271672995755493618039875576148888210813721562678209646202536778928064483731718316903925098423712814078626664762373015567892204457096563945050397
pinv = 52630128849197720680110472750445748362139896176637531822954326517425311680825011848954897216473363639703824050855325538315083014164303720747822395846650319695987688095158291151432519169084976930868513752588843713777689684275678356428411139716649262621622630997667298885499028563774054074332173540631319889597
qinv = 125496020857340618196277467222560283660900711303887368456426113439542149083570089122371450654613560708642271914201563769861679957096301702280557251661400261492798741353567063566155829049341500619204353629584549900179004920653223519411783060452352992381122206770893349104129009388564667579089451723604618440661
c = 1388762168166138453533502616535682311951662267796048439821372408514940452694372071133694678245859456415197350818844276387350533386163112380861811751402336635782785232530966339596198327482130002361308263664042358292425147457255505567604410008496199212314343371169549624681927057257495930259138537298520078715021539399084541293912853620643211368004457657505213763568639450075510208834704577814321673791370846192405275347289307606311671974787456421561549138384739624650167355754827475547501943429992429550124101325788544890357396437738989658781888433583926568899431456535167649223812165614500609693719689242432567228419

m = binascii.unhexlify(hex(pow(c,dp,p))[2:]).decode('utf-8')

print (m)