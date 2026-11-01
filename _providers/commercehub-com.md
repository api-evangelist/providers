---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/commercehub-com/conformance/commercehub-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/commercehub-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/commercehub-com/well-known/commercehub-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/commercehub-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/commercehub-com/hosts/commercehub-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/commercehub-com-hosts.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rithum.com/blog/pricing-best-practices-on-e-commerce-marketplaces/
- group: company
  title: ''
  type: Newsroom
  url: https://www.rithum.com/press/
- group: other
  title: ''
  type: Leadership
  url: https://www.rithum.com/company/leadership/
- group: start
  title: ''
  type: DeveloperPortal
  url: http://dev.rithum.com
- group: docs
  title: ''
  type: Documentation
  url: https://dev.rithum.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rithum
- group: auth
  href: https://artifacts.apis.io/commercehub-com/security/commercehub-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/commercehub-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rithum.com/
- group: company
  title: ''
  type: Blog
  url: https://www.rithum.com/blog/
- group: commercial
  title: ''
  type: TermsOfUse
  url: https://www.rithum.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rithum.com/privacy-policy/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://knowledge.rithum.com/mcp/v1
  - status: 200
    url: https://www.rithum.com/
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Rithum is a commerce platform that provides B2B e‑commerce solutions, enabling brands and retailers to build, manage, and scale online storefronts. The company offers tools for product catalog management, order processing, inventory synchronization, and integrations with ERP and fulfillment services. Rithum focuses on delivering a flexible, API‑first architecture that supports custom workflows, omnichannel experiences, and real‑time analytics for merchants seeking to grow their digital sales channels.
layout: provider
modified: '2026-10-22'
name: Rithum
nav: Providers
network: true
overview: 'Rithum is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Commerce, B2B, E-commerce, API, and Platform.


  Rithum''s developer surface includes pricing, documentation, engineering blog, and 11 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Commercehub Com Domain Security
  slug: commercehub-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: commercehub-com
tags:
- Commerce
- B2B
- E-commerce
- API
- Platform
website: https://www.rithum.com/
---
