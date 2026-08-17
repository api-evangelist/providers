---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/foresight-mental-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://foresightmentalhealth.com/
- group: company
  title: ''
  type: About
  url: https://foresightmentalhealth.com/about/
- group: company
  title: ''
  type: Blog
  url: https://foresightmentalhealth.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://foresightmentalhealth.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://foresightmentalhealth.com/patient-information/contact-us/
- group: start
  title: ''
  type: Login
  url: https://pp-wfe-102.advancedmd.com/account/logon
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://foresightmentalhealth.com/privacy-policy/
- group: company
  title: ''
  type: Careers
  url: https://foresightmentalhealth.com/about/join-our-team/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ForesightMentalHealth
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/foresightmentalhealth
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/foresight-mental-health-stock
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/foresight-mental-health-llms.txt
coverage:
  checked: '2026-08-16'
  detail: Foresight Mental Health buys its clinical technology rather than shipping it — scheduling runs on Zocdoc and the patient portals belong to AdvancedMD (California) and athenahealth (elsewhere), so there is no first-party API to document; no api./developer./docs./app./portal. hostname resolves in DNS, every /.well-known/ path 404s, and the only machine-readable documents on foresightmentalhealth.com are a Yoast-generated llms.txt, the sitemap index and the marketing site's stock WordPress core REST API at /wp-json/.
  evidence:
  - status: 200
    url: https://foresightmentalhealth.com/llms.txt
  - status: 200
    url: https://foresightmentalhealth.com/wp-json/
  - status: 404
    url: https://foresightmentalhealth.com/openapi.json
  - status: 404
    url: https://foresightmentalhealth.com/swagger.json
  - status: 404
    url: https://foresightmentalhealth.com/graphql
  - status: 404
    url: https://foresightmentalhealth.com/api-docs
  - status: 404
    url: https://foresightmentalhealth.com/.well-known/agent-card.json
  - status: 404
    url: https://foresightmentalhealth.com/.well-known/agent.json
  - status: 404
    url: https://foresightmentalhealth.com/.well-known/security.txt
  - status: 404
    url: https://foresightmentalhealth.com/mcp
  reason: no-developer-program
  state: none
created: '2026-08-16'
description: 'Foresight Mental Health is a Berkeley, California technology-enabled outpatient behavioral health organization founded in 2018 by UC Berkeley computer science students Doug Hapeman and Matt Milford to widen access to insurance-covered therapy and psychiatry. It delivers virtual and in-person care through its own clinics in California and Georgia plus partner locations in Arizona, Florida and Texas, covering psychiatry and medication management, individual and couples therapy (CBT, DBT-informed care, EMDR, ACT, Gottman Method, play therapy), child and adolescent services, a maternal mental health program, ADHD/IVA-2 CPT testing, intensive outpatient services in California and transcranial magnetic stimulation in Georgia. The company acquired Psychiatric Addictive Curative Therapies (PACT) Atlanta and has raised roughly $17.7M across pre-seed through Series C with investors including Polaris Partners. Its clinical technology stack is bought rather than built and patient-facing:
  scheduling runs through Zocdoc and the patient portals are operated by third parties — AdvancedMD for California patients and athenahealth elsewhere. Foresight publishes no developer program, no API documentation, and no machine-readable API contract; the only machine-readable documents on its host are a Yoast-generated llms.txt, a sitemap index and the marketing site''s stock WordPress core REST API at /wp-json/.'
image: https://foresightmentalhealth.com/wp-content/uploads/2023/04/foresight-logo-green.png
layout: provider
modified: '2026-08-16'
name: Foresight Mental Health
nav: Providers
network: true
overview: 'Foresight Mental Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Care, Mental Health, Behavioral Health, and Telehealth.


  Foresight Mental Health''s developer surface includes engineering blog, support, and 11 more developer resources.'
random_paper: 97
score:
  band: minimal
  composite: 12.5
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
security:
- kind: domain-security
  name: Foresight Mental Health Domain Security
  slug: foresight-mental-health-domain-security
  summary_line: TLSv1.3 · DMARC
slug: foresight-mental-health
tags:
- Company
- Health Care
- Mental Health
- Behavioral Health
- Telehealth
- Psychiatry
- Therapy
- Digital Health
- Outpatient Care
- Insurance
website: https://foresightmentalhealth.com/
---
