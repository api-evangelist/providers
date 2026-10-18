---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.1
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Terra Bio Agentic Access
  operation_count: 1
  slug: terra-bio-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: The public API from Terra — 1 operation(s) for public.
  name: Terra Public API
  slug: terra-bio-public-api
artifact_total: 5
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/terra-bio/refs/heads/main/agentic-access/terra-bio-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/terra-bio-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/terra-bio/refs/heads/main/rules/terra-bio-rules.yml
  title: ''
  type: Spectral
  url: rules/terra-bio-rules.yml
- group: auth
  title: ''
  type: Compliance
  url: https://terra.bio/customer-security-requirements/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/terra-bio/refs/heads/main/conformance/terra-bio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/terra-bio-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/terra-bio/refs/heads/main/hosts/terra-bio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/terra-bio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/terra-bio/refs/heads/main/vendors/terra-bio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/terra-bio-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://terra.bio/register-for-ashg-interactive-workshops/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/terra-bio/refs/heads/main/security/terra-bio-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/terra-bio-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/terra-bio/refs/heads/main/security/terra-bio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/terra-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://terra.bio
- group: docs
  title: ''
  type: Documentation
  url: https://terra.bio/terra-details/
- group: docs
  title: ''
  type: APIReference
  url: https://app.terra.bio/
- group: start
  title: ''
  type: GettingStarted
  url: https://terra.bio/get-started-with-free-cloud-credits/
- group: operate
  title: ''
  type: Support
  url: https://support.terra.bio/hc/en-us/sections/23504885621787
- group: company
  title: ''
  type: Blog
  url: https://terra.bio/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DataBiosphere/
- group: operate
  title: ''
  type: Roadmap
  url: https://terra.bio/introducing-the-public-terra-roadmap-shaping-the-future-together/
- group: commercial
  title: ''
  type: Pricing
  url: https://terra.bio/terra-plans/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://terra.bio/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://terra.bio/cookie-policy-us/?cmplz_region_redirect=true
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/terra-bio/workspace/terra-bio
created: '2026-10-14'
description: Terra is a leading platform for biomedical data analysis, secure sharing, and global collaboration. It provides researchers with tools to access, analyze, and share petabytes of biomedical data securely, supporting data sovereignty and collaborative science at scale. Terra enables secure data management, extensive computational tools, and a collaborative environment for clinicians and scientists worldwide.
image: https://terra.bio/wp-content/uploads/2023/12/TerraonAzure.png
layout: provider
modified: '2026-10-14'
name: Terra
nav: Providers
network: true
overview: 'Terra publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Company, Biomedical, DataAnalysis, Collaboration, and CloudPlatform.


  The Terra catalog on APIs.io includes 1 Spectral governance ruleset.


  Terra''s developer surface includes signup flow, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 14 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Terra API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: terra-bio-rules
score:
  band: thin
  composite: 37.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 31.5
    catalog_earned_first_party: 0.0
    catalog_gap: 83.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 32.4
    developer_ergonomics: 40.5
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Terra Bio Domain Security
  slug: terra-bio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Terra Bio Trust Center
  slug: terra-bio-trust-center
  summary_line: HIPAA, FedRAMP, GDPR, FIPS 140
slug: terra-bio
tags:
- Company
- Biomedical
- DataAnalysis
- Collaboration
- CloudPlatform
website: https://terra.bio
---
