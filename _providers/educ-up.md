---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-17'
  detail: The only software Educ-up operates is an end-user Moodle LMS at formation.edacademy.fr for enrolled Edacademy learners — its stock Moodle web-service endpoint answers 200 with errorcode "invalidtoken" but is Moodle's contract, token-gated and undocumented by Educ-up — while the corporate domain educ-up.fr now 302s to an IONOS parked page that returns the same 336-byte body for every path including nonsense ones, and the Domissori (WordPress) and Edacademy (Webflow) marketing sites carry no developer portal, no API reference and no spec at any probed location.
  evidence:
  - status: 200
    url: https://educ-up.fr/
  - status: 200
    url: https://educ-up.fr/.well-known/zzz-control-9f3k
  - status: 404
    url: https://domissori.fr/openapi.json
  - status: 404
    url: https://domissori.fr/.well-known/agent-card.json
  - status: 404
    url: https://www.edacademy.fr/llms.txt
  - status: 404
    url: https://www.edacademy.fr/.well-known/agent-card.json
  - status: 404
    url: https://formation.edacademy.fr/openapi.json
  - status: 200
    url: https://formation.edacademy.fr/webservice/rest/server.php?wsfunction=core_webservice_get_site_info
  - status: 404
    url: https://educ-up.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-08-17'
description: 'Educ-up is a French social-impact education group founded in 2016 by Mohamed El Mazzouji, headquartered in Saint-Denis, La Réunion with establishments in metropolitan France including Montreuil (Seine-Saint-Denis). It operates two consumer- and professional-facing brands rather than a software product: Domissori, launched in 2019, which places Montessori-trained educators in family homes for childcare, educational workshops and academic tutoring across Vannes, Chambéry, Lyon, Grenoble, Perpignan, Montpellier, Marseille and Saint-Denis; and Edacademy, a Qualiopi-certified training and apprenticeship centre for early-childhood and personal-care professions (CAP AEPE, Titre Pro ADVF, Bac Pro ASSP, parenting and Montessori support). The group also runs Ed''solidaire, a subsidy scheme that opens paid childcare to low-income families. Investors include Serena, M Capital, Inco Ventures, MakeSense and Racine2. Edacademy delivers its programmes through a self-hosted Moodle learning
  platform at formation.edacademy.fr, but that is an end-user LMS: as of August 2026 Educ-up publishes no developer portal, no API documentation and no machine-readable API contract, and its corporate domain educ-up.fr now redirects to a parked IONOS default site.'
layout: provider
modified: '2026-08-17'
name: Educ-up
nav: Providers
network: true
random_paper: 95
slug: educ-up
tags:
- Company
- Edtech
- Education
- Childcare
- Training
- Montessori
- Vocational Training
- France
- Social Impact
---
