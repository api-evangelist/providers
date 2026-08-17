---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-17'
  detail: Acheel's own partner FAQ answered "Avez-vous des APIs ?" with "nous mettons à votre disposition nos APIs", but that partner site (partners.acheel.com) now 301s to the Charlee broker marketing brand and the only route to the API is the broker partnership form at charlee.fr/registration — no reference, no base URL and no spec was ever published, and the broker console back.charlee.fr is a noindex login.
  evidence:
  - status: 301
    url: https://partners.acheel.com/
  - status: 200
    url: https://www.charlee.fr/registration
  - status: 200
    url: https://back.charlee.fr/
  - status: 404
    url: https://v2.acheel.com/openapi.json
  - status: 0
    url: https://api.acheel.com/
  reason: sales-gate
  state: gated
created: '2026-08-17'
description: 'Acheel is a French digital insurance company — a néo-assureur that carries its own insurance licence rather than broking someone else''s. Founded in 2020 by Ralph Ruimy and Francky Défossé, it received its ACPR agrément and launched in 2021, and now reports more than 800,000 policyholders. ACHEEL SA (879 605 350 RCS Paris) underwrites; ACHEEL FRANCE (ORIAS 21003575) distributes. The range spans nine lines — habitation, auto, santé, animaux, PNO (propriétaire non occupant), emprunteur, scolaire, protection juridique and RC pro — sold 100% digitally, with a quote in about two minutes and subscription in five. Roughly 70% of revenue comes from B2B2C distribution: partner brokers are served under the Charlee brand (charlee.fr, broker portal "Acheel Omega" at back.charlee.fr) and partners embed a per-tenant white-label customer area served from *.widget.acheel.com. Acheel''s own partner FAQ stated it makes its APIs available to partners ("nous mettons à votre disposition nos APIs
  afin de vous faire bénéficier de notre Tech et de nos produits"), but no developer portal, API reference, base URL or machine-readable specification is published anywhere on its public surface; API access travels with a brokerage partnership. Acheel is a certified B Corp.'
image: https://v2.acheel.com/assets/images/footer/acheel_footer_logo.svg
layout: provider
modified: '2026-08-17'
name: Acheel
nav: Providers
network: true
random_paper: 14
slug: acheel
tags:
- Company
- Fintech Insurtech
- Insurance
- Insurtech
- Digital Insurance
- Home Insurance
- Auto Insurance
- Health Insurance
- Pet Insurance
- White Label
- B2B2C
- Embedded Insurance
- France
---
