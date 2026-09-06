---
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
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/6cloudtechnology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.6cloudtech.com/
- group: company
  title: ''
  type: Blog
  url: https://www.6cloudtech.com/portal/index/news/pagename/page_news_dynamic.html
- group: operate
  title: ''
  type: Support
  url: https://www.6cloudtech.com/portal/index/aboutus/pagename/page_contact_us.html
- group: other
  title: ''
  type: WhitePapers
  url: https://www.6cloudtech.com/portal/index/cooperat/pagename/page_white.html
- group: other
  title: ''
  type: Research
  url: https://www.6cloudtech.com/portal/index/weekly/pagename/page_safe_warnning.html
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/6cloudtechnology-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/6cloudtechnology-plans-pricing.yml
coverage:
  checked: '2026-09-05'
  detail: 6Cloud Technology sells industrial-security appliances and platforms through a direct sales motion and publishes no developer surface at all — its own 1,031-URL sitemap contains no developer, API, reference or SDK page, and the closest thing to an integration contract it ships is a set of syslog log-format PDFs released only through a contact-capture form.
  evidence:
  - status: 200
    url: https://www.6cloudtech.com/sitemap.xml
  - status: 404
    url: https://www.6cloudtech.com/openapi.json
  - status: 404
    url: https://www.6cloudtech.com/.well-known/agent-card.json
  - status: 200
    url: https://www.6cloudtech.com/portal/index/cooperat/pagename/page_logfile.html
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: '6Cloud Technology (Chinese name 六方云; legal entity Beijing 6Cloud Information Technology Co., Ltd. / 北京六方云信息技术有限公司) is a Beijing-based industrial and critical-infrastructure cybersecurity product vendor founded in 2018 and backed by China''s Ministry of Science and Technology results-transformation fund. It builds and sells appliances and platforms across five product lines plus a security-services practice: industrial control security (LinSec — industrial firewall, industrial network audit and intrusion detection, industrial host guard, data diode/gateway, vulnerability scanner, asset and risk management), network security (NSec — next-generation firewall, IPS, IDS, operations management and audit, log audit and analysis, database audit), cloud security (CSec — distributed virtual firewall, distributed virtual IDS, cloud security resource scheduling), AI security (AiSec — network threat detection and retrospection), and situational-awareness security (CdSec — industrial situational
  awareness and security operations platform), alongside simulation and training range systems. It markets under an "AI gene, threat immunity" positioning and sells into rail transit, power, oil and gas and petrochemicals, public services, water conservancy, intelligent manufacturing, and smart mining. Products are delivered as vendor-sold appliances and platforms; the company publishes no public developer program, API reference, or machine-readable specification.'
image: https://www.6cloudtech.com/themes/6cloud/public/assets/img/logo.png
layout: provider
modified: '2026-09-05'
name: 6Cloud Technology
nav: Providers
network: true
overview: '6Cloud Technology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Industrial Control Systems, and Operational Technology.


  6Cloud Technology''s developer surface includes engineering blog, support, and 6 more developer resources.'
plans:
- name: 6Cloudtechnology Plans Pricing
  plan_count: 0
  slug: 6cloudtechnology-plans-pricing
random_paper: 14
score:
  band: minimal
  composite: 6.4
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 6Cloudtechnology Domain Security
  slug: 6cloudtechnology-domain-security
  summary_line: TLSv1.3
slug: 6cloudtechnology
tags:
- Company
- Security
- Cybersecurity
- Industrial Control Systems
- Operational Technology
- Critical Infrastructure
- Network Security
- Cloud Security
- Artificial Intelligence
- Firewall
- Intrusion Detection
- China
website: https://www.6cloudtech.com/
---
