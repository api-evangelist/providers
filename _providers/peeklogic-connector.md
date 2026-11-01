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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/peeklogic-connector/well-known/peeklogic-connector-peeklogic-connector-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/peeklogic-connector-peeklogic-connector-security.txt
- group: commercial
  href: https://artifacts.apis.io/peeklogic-connector/plans/peeklogic-connector-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/peeklogic-connector-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://www.peeklogic-connector.com/security-policy
- group: design
  href: https://artifacts.apis.io/peeklogic-connector/conformance/peeklogic-connector-conformance.yml
  title: ''
  type: Conformance
  url: conformance/peeklogic-connector-conformance.yml
- group: agent
  href: https://artifacts.apis.io/peeklogic-connector/llms/peeklogic-connector-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/peeklogic-connector-llms.txt
- group: auth
  href: https://artifacts.apis.io/peeklogic-connector/well-known/peeklogic-connector-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/peeklogic-connector-www-security.txt
- group: auth
  href: https://artifacts.apis.io/peeklogic-connector/well-known/peeklogic-connector-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/peeklogic-connector-security.txt
- group: agent
  href: https://artifacts.apis.io/peeklogic-connector/well-known/peeklogic-connector-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/peeklogic-connector-well-known.yml
- group: other
  href: https://artifacts.apis.io/peeklogic-connector/hosts/peeklogic-connector-hosts.yml
  title: ''
  type: Hosts
  url: hosts/peeklogic-connector-hosts.yml
- group: other
  href: https://artifacts.apis.io/peeklogic-connector/vendors/peeklogic-connector-vendors.yml
  title: ''
  type: Vendors
  url: vendors/peeklogic-connector-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.peeklogic-connector.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.peeklogic-connector.com/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://www.peeklogic-connector.com/documentation/
- group: company
  title: ''
  type: Blog
  url: https://www.peeklogic-connector.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.peeklogic-connector.com/blog/hr-onboarding-software/
- group: auth
  href: https://artifacts.apis.io/peeklogic-connector/security/peeklogic-connector-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/peeklogic-connector-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/peeklogic-connector/security/peeklogic-connector-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/peeklogic-connector-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://peeklogic-connector.com/
coverage:
  checked: '2026-10-21'
  detail: The provider's documentation site serves only HTML pages with no machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL specifications.
  evidence:
  - status: 200
    url: https://www.peeklogic-connector.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: Peeklogic Connector is a growing collection of integration tools that help businesses connect Salesforce with their other essential systems. It offers connectors for Jira, NetSuite, Azure DevOps, HubSpot, and more, streamlining workflows and boosting productivity. The platform continuously adds new connectors to facilitate seamless data synchronization across enterprise applications.
image: https://www.peeklogic-connector.com/wp-content/uploads/2026/01/peeklogic-connectors-logo.svg
layout: provider
modified: '2026-10-21'
name: Peeklogic
nav: Providers
network: true
overview: 'Peeklogic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Integration, Salesforce, Connector, Automation, and Enterprise.


  Peeklogic''s developer surface includes pricing, documentation, engineering blog, getting-started guide, and 14 more developer resources.'
plans:
- name: Peeklogic Connector Plans Pricing
  plan_count: 13
  slug: peeklogic-connector-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Peeklogic Connector Domain Security
  slug: peeklogic-connector-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Peeklogic Connector Vulnerability Disclosure
  slug: peeklogic-connector-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: peeklogic-connector
tags:
- Integration
- Salesforce
- Connector
- Automation
- Enterprise
website: https://peeklogic-connector.com/
---
