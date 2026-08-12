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
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paige-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.paige.ai/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/paige_stock/
- group: company
  title: ''
  type: About
  url: https://www.paige.ai/about
- group: company
  title: ''
  type: Blog
  url: https://www.paige.ai/blog
- group: company
  title: ''
  type: News
  url: https://www.paige.ai/news
- group: operate
  title: ''
  type: PressReleases
  url: https://www.paige.ai/press-releases
- group: operate
  title: ''
  type: Support
  url: https://support.paige.ai/
- group: start
  title: ''
  type: SignUp
  url: https://www.paige.ai/request-a-trial
- group: start
  title: ''
  type: Login
  url: https://app.paige.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.paige.ai/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.paige.ai/privacy-policy-1
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Paige-AI
- group: auth
  title: ''
  type: Compliance
  url: https://www.paige.ai/ai-technology-and-services
- group: design
  title: ''
  type: Conformance
  url: conformance/paige-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/paige-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/paige-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/paige-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/paige-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/paige-llms.txt
coverage:
  checked: '2026-08-04'
  detail: Paige markets "UnifAI" (an SDK plus APIs powering its AppLab marketplace) but ships that surface only to laboratory customers — its developer documentation host docs.paige.ai is CNAMEd to ReadMe.io yet returns Cloudflare error 1014 for every path, api.paige.ai/developer.paige.ai/unifai.paige.ai do not resolve at all, and the only public entry point is a "Request a trial" sales form.
  evidence:
  - status: 403
    url: https://docs.paige.ai/
  - status: 403
    url: https://docs.paige.ai/openapi.json
  - status: 404
    url: https://www.paige.ai/llms.txt
  - status: 404
    url: https://www.paige.ai/.well-known/security.txt
  - status: 200
    url: https://www.paige.ai/request-a-trial
  reason: customer-only-docs
  state: gated
created: '2026-08-04'
description: 'Paige (Paige AI, Inc.) is a New York City computational-pathology company founded in 2017 out of Memorial Sloan Kettering, and the first company to receive FDA authorization for a clinical AI application in digital pathology (Paige Prostate, De Novo 2021) alongside the FDA-cleared FullFocus whole-slide-image viewer. Its product line spans the Paige Platform, the Alba pathology copilot, OmniScreen, the AppLab third-party AI marketplace, and the openly published Virchow / Virchow2 / PRISM foundation-model family. Paige markets "UnifAI" — an SDK plus a set of APIs for vendor-neutral integration into laboratory workflows — but that developer surface is sold to laboratory customers rather than published: the developer docs host docs.paige.ai no longer resolves for the public. What Paige does publish openly is its research stack: the Paige-AI GitHub organization (paige-ml-sdk, philips-isyntax-rs, cdh1-cancer-res, omniscreen-eval-results) and the paige-ai Hugging Face organization
  carrying the Virchow and PRISM model weights. Paige was acquired by Tempus AI in September 2025.'
image: https://static1.squarespace.com/static/67cf140aa73e796561bb793f/t/67cf195030a3f94d4263b55d/1741625680290/Asset+1.png?format=1500w
layout: provider
modified: '2026-08-04'
name: Paige
nav: Providers
network: true
overview: 'Paige is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine Learning, Healthcare, and Health.


  Paige''s developer surface includes engineering blog, product news, support, signup flow, CLI, changelog, and 14 more developer resources.'
random_paper: 54
score:
  band: emerging
  composite: 24.4
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 24.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paige/refs/heads/main/screenshots/paige-2026-08-07T191306.png
security:
- kind: domain-security
  name: Paige Domain Security
  slug: paige-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: paige
tags:
- Company
- Artificial Intelligence
- Machine Learning
- Healthcare
- Health
- Digital Pathology
- Medical Imaging
- Oncology
- Diagnostics
- Life Sciences
- Foundation Models
- Medical Devices
website: https://www.paige.ai/
---
