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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/balthasarspeyr-org/hosts/balthasarspeyr-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/balthasarspeyr-org-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.balthasarspeyr.org/legal/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.balthasarspeyr.org/legal/privacy-policy
- group: auth
  href: https://artifacts.apis.io/balthasarspeyr-org/security/balthasarspeyr-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/balthasarspeyr-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://balthasarspeyr.org/
coverage:
  checked: '2026-11-02'
  detail: The provider offers a theological publications portal with no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://balthasarspeyr.org/
  reason: no-developer-program
  state: none
created: '2026-11-02'
description: Balthasar & Speyr is a dedicated portal offering a curated collection of publications by the renowned theologians Hans Urs von Balthasar and Adrienne von Speyr. The site provides access to books, articles, and scholarly works in both print and electronic formats, serving scholars, students, and anyone interested in contemporary Catholic theology and spirituality. It also features news, events, and resources related to the authors' legacy.
image: https://balthasarspeyr.org/_next/static/media/index-04.0fed15e2.jpg
layout: provider
modified: '2026-11-02'
name: Balthasar & Speyr
nav: Providers
network: true
overview: Balthasar & Speyr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Theology, Publications, Books, Hans Urs von Balthasar, and Adrienne von Speyr.
random_paper: 10
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 8.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Balthasarspeyr Org Domain Security
  slug: balthasarspeyr-org-domain-security
  summary_line: TLSv1.3 · DMARC
slug: balthasarspeyr-org
tags:
- Theology
- Publications
- Books
- Hans Urs von Balthasar
- Adrienne von Speyr
website: https://balthasarspeyr.org/
---
