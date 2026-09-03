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
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/precision-neuroscience/layer7-nbme2025/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/precision-neuroscience/layer7-nbme2025/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/precision-neuroscience-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.precisionneuro.io/
- group: other
  title: ''
  type: Technology
  url: https://www.precisionneuro.io/our-technology
- group: company
  title: ''
  type: News
  url: https://www.precisionneuro.io/articles
- group: company
  title: ''
  type: Blog
  url: https://www.precisionneuro.io/articles/company-news
- group: other
  title: ''
  type: Research
  url: https://www.precisionneuro.io/articles/research
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/precision-neuroscience
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/precision-neuroscience/layer7-nbme2025
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/precision-neuroscience-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/precision-neuroscience-conformance.yml
- group: company
  title: ''
  type: Careers
  url: https://www.precisionneuro.io/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.precisionneuro.io/contact
- group: company
  title: ''
  type: Partners
  url: https://www.precisionneuro.io/partner-with-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.precisionneuro.io/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.precisionneuro.io/privacy-policy
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/precision-neuroscience_stock/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/precision-neuroscience-corporation
coverage:
  checked: '2026-08-05'
  detail: 'Precision Neuroscience ships an FDA-cleared implantable medical device and runs no developer program — every /.well-known/ path, /llms.txt, /openapi.json and /graphql returns a Next.js 404 on www.precisionneuro.io, no api./developer./portal./status. host resolves, the only docs host that does resolve (docs.precisionneuro.io) is a PRIVATE GitHub Pages site that 302s to github.com/pages/auth, and the company''s verified GitHub org holds exactly one public repo: an Apache-2.0 research notebook.'
  evidence:
  - status: 404
    url: https://www.precisionneuro.io/openapi.json
  - status: 404
    url: https://www.precisionneuro.io/llms.txt
  - status: 404
    url: https://www.precisionneuro.io/.well-known/agent-card.json
  - status: 302
    url: https://docs.precisionneuro.io/
  - status: 200
    url: https://api.github.com/orgs/precision-neuroscience/repos
  reason: no-developer-program
  state: none
created: '2026-08-05'
description: 'Precision Neuroscience is a New York City brain-computer interface company founded in 2021 by Benjamin Rapoport, Michael Mager, Demetrios Papageorgiou and Mark Hettick, with additional sites in Santa Clara, California and Addison, Texas. Its product is the Layer 7 Cortical Interface, a thin-film microelectrode array that lies on the surface of the cortex rather than penetrating brain tissue, and is designed to be removable and upgradable. The array received FDA 510(k) clearance for recording, monitoring and stimulating on the brain surface for implantation durations of up to 30 days, and the company reports 95+ clinical study participants across 15+ hospital partnerships — Mount Sinai, Penn Medicine, Johns Hopkins, Mass General Brigham, Northwestern, Emory, Barrow Neurological Institute and others — plus a strategic partnership with Medtronic. Precision sells a regulated medical device, not software services. It runs no developer program: no public API, SDK, webhooks, developer
  portal or machine-readable specification is published anywhere on its domain. Its only public engineering surface is a verified GitHub organization whose single public repository is an Apache-2.0 research notebook accompanying a 2025 neural-decoding result.'
image: https://cdn.sanity.io/images/883wn8od/production/27b30ec3135c38d300a7ad288ad4d71b142bdcd1-1200x630.png?fm=webp&w=1200&q=75
layout: provider
modified: '2026-08-05'
name: Precision Neuroscience
nav: Providers
network: true
overview: 'Precision Neuroscience is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Brain-Computer Interface, Neurotechnology, Medical Devices, and Neuroscience.


  Precision Neuroscience''s developer surface includes product news, engineering blog, and 17 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 4.5
    operational_transparency: 2.6
  open_source:
    applies: true
    score: 0.0
  previous_composite: 11.0
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/precision-neuroscience/refs/heads/main/screenshots/precision-neuroscience-2026-09-02T151910.png
security:
- kind: domain-security
  name: Precision Neuroscience Domain Security
  slug: precision-neuroscience-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: precision-neuroscience
tags:
- Company
- Brain-Computer Interface
- Neurotechnology
- Medical Devices
- Neuroscience
- Implantable Devices
- neural-interfaces
- Health Technology
- Clinical Research
- Deep Tech
website: https://www.precisionneuro.io/
---
