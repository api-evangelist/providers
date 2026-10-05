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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://a16z.com/security-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/andreessenhorowitz/refs/heads/main/well-known/andreessenhorowitz-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/andreessenhorowitz-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/andreessenhorowitz/refs/heads/main/well-known/andreessenhorowitz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/andreessenhorowitz-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/andreessenhorowitz/refs/heads/main/hosts/andreessenhorowitz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/andreessenhorowitz-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/andreessenhorowitz/refs/heads/main/vendors/andreessenhorowitz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/andreessenhorowitz-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://a16z.com/team/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/andreessenhorowitz/refs/heads/main/security/andreessenhorowitz-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/andreessenhorowitz-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/andreessenhorowitz/refs/heads/main/security/andreessenhorowitz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/andreessenhorowitz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://a16z.com
- group: docs
  title: ''
  type: APIReference
  url: https://a16z.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://a16z.com/about
- group: operate
  title: ''
  type: Support
  url: https://a16z.com/supporting-the-open-source-ai-community/
- group: company
  title: ''
  type: Blog
  url: https://a16z.com/news-content
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/a16z
- group: commercial
  title: ''
  type: TermsOfService
  url: https://a16z.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://a16z.com/privacy-policy
coverage:
  checked: 2026-09-24
  detail: Developer portal at https://a16z.com/enterprise/developer-tooling provides no OpenAPI or other machine‑readable contract.
  evidence:
  - status: 301
    url: https://a16z.com/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-24'
description: Andreessen Horowitz (a16z) is a leading venture capital firm investing in technology companies across various sectors including AI, bio‑health, consumer, crypto, enterprise, fintech, and infrastructure. The firm publishes insights, research, and resources for founders and developers, and maintains a robust online presence with sections for portfolio, team, focus areas, news, and a dedicated developer portal offering guides, tooling insights, and API resources.
image: https://d1lamhf6l6yk6d.cloudfront.net/uploads/2026/03/a16z-Yoast-LI.png
layout: provider
modified: '2026-09-24'
name: Andreessenhorowitz
nav: Providers
network: true
overview: 'Andreessenhorowitz is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Venture Capital, Technology, Investment, Artificial Intelligence, and Bio-Health.


  Andreessenhorowitz''s developer surface includes API reference, getting-started guide, support, engineering blog, and 12 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 50.0
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Andreessenhorowitz Domain Security
  slug: andreessenhorowitz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Andreessenhorowitz Vulnerability Disclosure
  slug: andreessenhorowitz-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: andreessenhorowitz
tags:
- Venture Capital
- Technology
- Investment
- Artificial Intelligence
- Bio-Health
website: https://a16z.com
---
