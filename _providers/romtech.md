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
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/romtech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://romtech.com/
- group: company
  title: ''
  type: About
  url: https://romtech.com/about-romtech/
- group: other
  title: ''
  type: Product
  url: https://romtech.com/portableconnect/
- group: company
  title: ''
  type: Blog
  url: https://romtech.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://romtech.com/feed/
- group: operate
  title: ''
  type: PressReleases
  url: https://romtech.com/press-releases/
- group: other
  title: ''
  type: MediaRoom
  url: https://romtech.com/romtech-media-room/
- group: operate
  title: ''
  type: Support
  url: https://romtech.com/contact-us/
- group: operate
  title: ''
  type: FAQ
  url: https://romtech.com/frequently-asked-questions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://romtech.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://romtech.com/terms/
- group: other
  title: ''
  type: Patents
  url: https://romtech.com/patents/
- group: company
  title: ''
  type: Careers
  url: https://www.paycomonline.net/v4/ats/web.php/portal/74B8425BF3D1B3ACB19CC1353DC5FA0E/career-page
- group: start
  title: ''
  type: ClinicianPortal
  url: https://portal.romtech.com/
- group: other
  title: ''
  type: GovernmentPurchasing
  url: https://romtech.com/veterans-affairs-purchasing/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/romtech-stock
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/romtechnologies
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ROMTechnologies
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UC0WlP8_td5Liz0Wq-TvdZ5Q
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/romtech_rehab/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/romtech-llms.txt
coverage:
  checked: '2026-08-26'
  detail: ROMTech ships real connected software — the PortableConnect device app, the AccuAngle wearable and a React Clinician Portal at portal.romtech.com — but only as a prescription end-user product, and the portal's own JavaScript bundle names its backend as a private, undocumented API at https://middleware.romtech.com/api/ that answers HTTP 500 on every discovery path (/swagger/v1/swagger.json, /openapi.json, /.well-known/*) while returning {"success":true,"data":"az-middleware"} on /api, so there is no published contract, SDK, or developer portal to catalog.
  evidence:
  - status: 404
    url: https://romtech.com/openapi.json
  - status: 404
    url: https://romtech.com/.well-known/agent-card.json
  - status: 404
    url: https://romtech.com/graphql
  - status: 200
    url: https://romtech.com/llms.txt
  - status: 200
    url: https://romtech.com/wp-json/
  - status: 200
    url: https://portal.romtech.com/openapi.json
  - status: 200
    url: https://middleware.romtech.com/api/
  - status: 500
    url: https://middleware.romtech.com/swagger/v1/swagger.json
  - status: 200
    url: https://connect.romtech.com/
  - status: 404
    url: https://api.github.com/orgs/romtech
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'ROMTech (ROM Technologies, Inc.) is a privately held medical technology company headquartered in Brookfield, Connecticut that builds connected orthopedic rehabilitation technology. Its flagship product, the PortableConnect Adaptive Telemed Technology, is a prescription, clinician-delivered home rehabilitation device for patients recovering from total knee replacement, total hip replacement, joint manipulation and ACL repair. Adaptive pedal technology adjusts automatically to a patient''s current range of motion across four therapy modes (passive, active-assisted, active and resistance); the AccuAngle Bluetooth wearable measures knee flexion and extension during each session; and the PortableConnect App runs a prescribed protocol of three to five daily sessions over a typical four-to-eight-week plan. Session data — range of motion, adherence and key health metrics — streams to a Clinician Portal where the prescribing surgeon reviews real-time reports and adjusts the protocol
  remotely, with in-app telemedicine for face-to-face follow-ups. The technology began as the ROM3 Rehab device. ROMTech was named to Fast Company''s Most Innovative Companies list for 2025 and to the LexisNexis Top 100 Global Innovators for 2026, and sells to clinicians, health systems and the Department of Veterans Affairs. ROMTech runs no public developer program: it publishes no OpenAPI, SDK, webhook catalog or developer documentation, and the Clinician Portal at portal.romtech.com is a closed single-page application backed by a private, undocumented API at middleware.romtech.com/api.'
image: https://romtech.com/wp-content/themes/romtech2021/img/logo.png
layout: provider
modified: '2026-08-26'
name: ROMTech
nav: Providers
network: true
overview: 'ROMTech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medical Devices, Rehabilitation, and Physical Therapy.


  ROMTech''s developer surface includes engineering blog, support, FAQ, YouTube channel, and 18 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/romtech/refs/heads/main/screenshots/romtech-2026-09-02T154109.png
security:
- kind: domain-security
  name: Romtech Domain Security
  slug: romtech-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: romtech
tags:
- Company
- Healthcare
- Medical Devices
- Rehabilitation
- Physical Therapy
- Telemedicine
- Remote Patient Monitoring
- Orthopedics
- Digital Health
- Connected Devices
- Wearables
website: https://romtech.com/
---
