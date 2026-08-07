---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cybersecurity And Infrastructure Security Agency Agentic Access
  operation_count: 3
  slug: cybersecurity-and-infrastructure-security-agency-agentic-access
  summary_line: 3 operations
api_count: 4
apis:
- description: CISA's Automated Indicator Sharing (AIS) program uses a TAXII 2.1 server to deliver STIX-formatted cyber threat indicators (CTI) and defensive measures (DM) to vetted partners. AIS includes AIS PUBLIC
  name: CISA Automated Indicator Sharing (AIS) TAXII Server
  slug: ais
- description: 'CISA publishes Cybersecurity Advisories (CSAs), Industrial Control Systems Advisories (ICSAs), and Common Security Advisory Framework (CSAF) JSON documents describing tactics, techniques, indicators, '
  name: CISA Cybersecurity Advisories
  slug: advisories
- description: Known Exploited Vulnerabilities catalog feed
  name: Cybersecurity and Infrastructure Security Agency KEV API
  slug: cybersecurity-and-infrastructure-security-agency-kev-api
- description: JSON Schema for the KEV catalog
  name: Cybersecurity and Infrastructure Security Agency Schema API
  slug: cybersecurity-and-infrastructure-security-agency-schema-api
artifact_total: 15
collections:
- collection_type: open
  name: CISA Known Exploited Vulnerabilities (KEV) Catalog API
  slug: open-cisa-kev
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cybersecurity-and-infrastructure-security-agency-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cybersecurity-and-infrastructure-security-agency-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cybersecurity-and-infrastructure-security-agency-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cisagov
- group: company
  title: ''
  type: Website
  url: https://www.cisa.gov
- group: other
  title: ''
  type: KEVCatalog
  url: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- group: other
  title: ''
  type: Advisories
  url: https://www.cisa.gov/news-events/cybersecurity-advisories
- group: other
  title: ''
  type: Topics
  url: https://www.cisa.gov/topics
- group: build
  title: ''
  type: ResourcesAndTools
  url: https://www.cisa.gov/resources-tools
- group: company
  title: ''
  type: NewsAndEvents
  url: https://www.cisa.gov/news-events
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cisagov
- group: other
  title: ''
  type: KEVDataMirror
  url: https://github.com/cisagov/kev-data
- group: operate
  title: ''
  type: ContactUs
  url: https://www.cisa.gov/about/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cisa.gov/privacy-policy
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cisa-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cisa-kev-vulnerability-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/cisa-vocabulary.yml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/cisa-kev-capabilities.yml
- group: design
  title: ''
  type: Rules
  url: rules/cisa-kev-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://www.cisa.gov/cybersecurity-advisories/all.xml
created: '2024-12-03'
description: The Cybersecurity and Infrastructure Security Agency (CISA) is the United States federal civilian cybersecurity agency, part of the Department of Homeland Security. CISA reduces cybersecurity and physical security risk for the nation, coordinates federal civilian cyber defense, and partners with state, local, tribal, and territorial governments and the private sector. CISA publishes a number of public, unauthenticated machine-readable feeds, including the Known Exploited Vulnerabilities (KEV) catalog (mandatorily remediated by federal civilian agencies under Binding Operational Directive 22-01), Cybersecurity Advisories, and Common Security Advisory Framework (CSAF) advisories. CISA also operates an Automated Indicator Sharing (AIS) TAXII 2.1 server that delivers STIX cyber threat indicators to vetted partners under a Terms of Use and Interconnection Agreement.
finops:
- name: Cybersecurity And Infrastructure Security Agency Finops
  service_category: API
  slug: cybersecurity-and-infrastructure-security-agency-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cybersecurity-and-infrastructure-security-agency.png
json_schemas:
- name: KevVulnerability
  property_count: 11
  slug: cisa-kev-vulnerability
jsonld:
- class_count: 18
  name: Cisa Context
  property_count: 0
  slug: cisa-context
layout: provider
modified: '2026-05-19'
name: Cybersecurity and Infrastructure Security Agency
nav: Providers
network: true
overview: 'Cybersecurity and Infrastructure Security Agency publishes 2 APIs on the [APIs.io](https://apis.io/) network: KEV API and Schema API. Tagged areas include Advisories, AIS, Binding Operational Directive, CSAF, and CVE.


  The Cybersecurity and Infrastructure Security Agency catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Cybersecurity and Infrastructure Security Agency''s developer surface includes engineering blog and 19 more developer resources.'
plans:
- name: Cybersecurity And Infrastructure Security Agency Plans Pricing
  plan_count: 3
  slug: cybersecurity-and-infrastructure-security-agency-plans-pricing
random_paper: 105
rate_limits:
- limit_count: 5
  name: Cybersecurity And Infrastructure Security Agency Rate Limits
  slug: cybersecurity-and-infrastructure-security-agency-rate-limits
rules:
- name: Cybersecurity and Infrastructure Security Agency API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: cisa-kev-rules
- name: Cybersecurity and Infrastructure Security Agency API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cybersecurity-and-infrastructure-security-agency-jsonschema-spectral-rules
score:
  band: thin
  composite: 41.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 65.9
    developer_ergonomics: 2.2
    discoverability: 64.8
    governance: 31.3
    operational_transparency: 36.8
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 38.9
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cybersecurity-and-infrastructure-security-agency/refs/heads/main/screenshots/cybersecurity-and-infrastructure-security-agency-2026-06-20T175408.png
security:
- kind: domain-security
  name: Cybersecurity And Infrastructure Security Agency Domain Security
  slug: cybersecurity-and-infrastructure-security-agency-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cybersecurity And Infrastructure Security Agency Vulnerability Disclosure
  slug: cybersecurity-and-infrastructure-security-agency-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cybersecurity-and-infrastructure-security-agency
tags:
- Advisories
- AIS
- Binding Operational Directive
- CSAF
- CVE
- CWE
- Cybersecurity
- Federal Government
- Government
- ICS-CERT
- Information Sharing
- KEV
- Known Exploited Vulnerabilities
- Risk Management
- Security
- STIX
- TAXII
- Threat Intelligence
- Vulnerability Management
website: https://www.cisa.gov
---
