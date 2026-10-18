---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.2
  scored_at: '2026-10-17'
api_count: 1
apis:
- baseURL: https://clinicalauditai.com/api/v1
  baseurl_source: declared
  description: Audit generation and retrieval
  name: ClinicalAuditAI Audits API
  slug: clinicalauditai-audits-api
- baseURL: https://clinicalauditai.com/api/v1
  baseurl_source: declared
  description: Client notification and webhook configuration
  name: ClinicalAuditAI Client Settings API
  slug: clinicalauditai-client-settings-api
- baseURL: https://clinicalauditai.com/api/v1
  baseurl_source: declared
  description: API health checks
  name: ClinicalAuditAI Health API
  slug: clinicalauditai-health-api
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/clinicalauditai/refs/heads/main/plans/clinicalauditai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clinicalauditai-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clinicalauditai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clinicalauditai/refs/heads/main/data-model/clinicalauditai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clinicalauditai-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clinicalauditai/refs/heads/main/errors/clinicalauditai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clinicalauditai-problem-types.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clinicalauditai/refs/heads/main/hosts/clinicalauditai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clinicalauditai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clinicalauditai/refs/heads/main/vendors/clinicalauditai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clinicalauditai-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clinicalauditai/refs/heads/main/security/clinicalauditai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clinicalauditai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clinicalauditai.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.clinicalauditai.com/api-audit-on-the-go.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clinicalauditai.com/pricing.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clinicalauditai.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clinicalauditai.com/privacy.html
- group: operate
  title: ''
  type: Support
  url: https://www.clinicalauditai.com/contact
created: '2026-10-05'
description: ClinicalAuditAI provides an API that automates the generation of clinical audit reports for CROs, sponsors, hospitals and quality assurance teams. Using a provisioned X‑API‑Key, clients can submit source data, receive structured audit results, PDF reports, and webhook notifications. The service aims to reduce audit preparation time, improve compliance scoring, and streamline inspection readiness across the healthcare research lifecycle.
layout: provider
modified: '2026-10-05'
name: ClinicalAuditAI
nav: Providers
network: true
overview: 'ClinicalAuditAI publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Audits API, Client Settings API, and Health API. Tagged areas include Company, Healthcare, Clinical Audits, and Automation.


  ClinicalAuditAI''s developer surface includes documentation, pricing, support, and 10 more developer resources.'
plans:
- name: Clinicalauditai Plans Pricing
  plan_count: 2
  slug: clinicalauditai-plans-pricing
random_paper: 6
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 38.0
    catalog_earned_first_party: 8.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 48.4
    developer_ergonomics: 16.1
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Clinicalauditai Domain Security
  slug: clinicalauditai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clinicalauditai
tags:
- Company
- Healthcare
- Clinical Audits
- Automation
website: https://www.clinicalauditai.com
---
