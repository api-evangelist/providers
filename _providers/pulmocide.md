---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pulmocide-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pulmocide-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pulmocide.com/
- group: company
  title: ''
  type: About
  url: https://pulmocide.com/about-us/
- group: operate
  title: ''
  type: Contact
  url: https://pulmocide.com/contact/
- group: company
  title: ''
  type: News
  url: https://pulmocide.com/in-the-news/
- group: company
  title: ''
  type: BlogRSS
  url: https://pulmocide.com/feed/
- group: company
  title: ''
  type: Investors
  url: https://pulmocide.com/investors-and-partners/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pulmocide.com/privacy-notice/
- group: other
  title: ''
  type: CookiePolicy
  url: https://pulmocide.com/cookie-policy/
- group: other
  title: ''
  type: Accessibility
  url: https://pulmocide.com/accessibility/
coverage:
  checked: '2026-08-26'
  detail: Pulmocide Ltd. is a clinical-stage biopharmaceutical company whose product is an inhaled antifungal drug (opelconazole), not software; its only web property is a twelve-page WordPress marketing site with no developer section, and every contract-discovery path on pulmocide.com (/openapi.json, /graphql, /llms.txt, every /.well-known/*) returned 404 while the site's stock WordPress /wp-json/ discovery root is default CMS plumbing rather than an API the company ships.
  evidence:
  - status: 404
    url: https://pulmocide.com/openapi.json
  - status: 404
    url: https://pulmocide.com/graphql
  - status: 404
    url: https://pulmocide.com/llms.txt
  - status: 404
    url: https://pulmocide.com/.well-known/agent-card.json
  - status: 200
    url: https://pulmocide.com/wp-json/
  - status: 404
    url: https://github.com/pulmocide
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'Pulmocide Ltd. is a privately held, clinical-stage biopharmaceutical company headquartered at 44 Southampton Buildings in London, United Kingdom, with a US entity (Pulmocide Inc.) in Boston, Massachusetts. It develops novel inhaled medicines for pulmonary aspergillosis and other difficult-to-treat respiratory diseases, delivering drug directly to the site of infection in the lung to achieve high local exposure with low systemic exposure. Its lead asset is opelconazole (formerly PC945), an inhaled triazole antifungal active against Aspergillus that has received US FDA Orphan Drug, Fast Track and Qualified Infectious Disease Product designations; the company reported Phase 2 OPERA-S safety results in 2024 and announced termination of the Phase 3 OPERA-T study in 2025. Pulmocide is a drug developer, not a software or platform company: it publishes no developer program, no public API, no SDKs and no machine-readable API contract of any kind. This profile therefore records identity,
  corporate web properties and probed absence rather than API artifacts.'
image: https://pulmocide.com/wp-content/uploads/2023/08/PULM_OG_Facebook.png
layout: provider
modified: '2026-08-26'
name: Pulmocide
nav: Providers
network: true
overview: 'Pulmocide is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Clinical Trials.


  Pulmocide''s developer surface includes product news and 10 more developer resources.'
random_paper: 17
screenshot: https://raw.githubusercontent.com/api-evangelist/pulmocide/refs/heads/main/screenshots/pulmocide-2026-09-02T152318.png
security:
- kind: domain-security
  name: Pulmocide Domain Security
  slug: pulmocide-domain-security
  summary_line: TLSv1.3
slug: pulmocide
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Clinical Trials
- Respiratory
- Antifungal
- Drug Development
- Healthcare
- United Kingdom
website: https://pulmocide.com/
---
