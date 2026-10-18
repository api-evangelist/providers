---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.3
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 246
  human_in_the_loop: 246
  name: Comp Ai Agentic Access
  operation_count: 412
  slug: comp-ai-agentic-access
  summary_line: 412 operations · 246 acting · 246 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Generate signed download links for files attached to compliance tasks, comments, evidence records, and workflow reviews.
  name: Comp AI Attachments API
  slug: comp-ai-attachments-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Retrieve audit trails for compliance activity, evidence changes, access decisions, and customer-facing security review workflows.
  name: Comp AI Audit Logs API
  slug: comp-ai-audit-logs-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Run AWS, Azure, and GCP cloud security scans, detect enabled services, review findings, and connect cloud posture results to compliance work.
  name: Comp AI Cloud Security API
  slug: comp-ai-cloudsecurity-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Create and manage collaboration comments on compliance entities such as tasks, policies, risks, vendors, and findings.
  name: Comp AI Comments API
  slug: comp-ai-comments-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Manage organization context that helps Comp AI tailor policies, assessments, and compliance automation to the business.
  name: Comp AI Context API
  slug: comp-ai-context-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Manage controls, map them to policies, tasks, framework requirements, and evidence document types, and track implementation progress.
  name: Comp AI Controls API
  slug: comp-ai-controls-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Register employee devices, submit device compliance check-ins, download agent builds, and manage endpoint security status.
  name: Comp AI Device Agent API
  slug: comp-ai-device-agent-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Read and manage employee device inventory and Fleet compliance data used for endpoint security controls.
  name: Comp AI Devices API
  slug: comp-ai-devices-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Export task evidence, automation evidence, and reviewer-ready evidence bundles as PDF or ZIP files.
  name: Comp AI Evidence Export API
  slug: comp-ai-evidence-export-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Export all organization evidence for an auditor review package.
  name: Comp AI Evidence Export (Auditor) API
  slug: comp-ai-evidence-export-auditor-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Collect, review, upload, and export structured evidence submissions for compliance tasks and document requirements.
  name: Comp AI Evidence Forms API
  slug: comp-ai-evidence-forms-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Create, review, update, and track audit findings, remediation activity, and finding history for an organization.
  name: Comp AI Findings API
  slug: comp-ai-findings-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Manage SOC 2, ISO 27001, HIPAA, GDPR, and custom framework instances, requirements, scores, and sync history.
  name: Comp AI Frameworks API
  slug: comp-ai-frameworks-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Connect vendor systems, configure OAuth apps, run compliance checks, sync employees, manage variables, and collect automated evidence.
  name: Comp AI Integrations API
  slug: comp-ai-integrations-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: The ISMS API from Comp AI — 17 operation(s) for isms.
  name: Comp AI ISMS API
  slug: comp-ai-isms-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Upload source documents, process them for retrieval, and manage reusable manual answers that power questionnaires and AI policy workflows.
  name: Comp AI Knowledge Base API
  slug: comp-ai-knowledge-base-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: The Offboarding Checklist API from Comp AI — 11 operation(s) for offboarding checklist.
  name: Comp AI Offboarding Checklist API
  slug: comp-ai-offboarding-checklist-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Manage organization chart metadata and evidence used for governance, accountability, and audit readiness.
  name: Comp AI Org Chart API
  slug: comp-ai-org-chart-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Manage organization profile data, API keys, logos, ownership, role notifications, and access approval settings.
  name: Comp AI Organization API
  slug: comp-ai-organization-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Invite and manage workforce members, training status, device compliance, email preferences, and employee evidence records.
  name: Comp AI People API
  slug: comp-ai-people-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Create, version, publish, export, map, and improve compliance policies with AI-assisted drafting and approval workflows.
  name: Comp AI Policies API
  slug: comp-ai-policies-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Parse security questionnaires, generate answers from approved evidence, save reviewer edits, stream progress, and export completed files.
  name: Comp AI Questionnaire API
  slug: comp-ai-questionnaire-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Create, update, and report on organizational risks with ownership, departments, and compliance remediation status.
  name: Comp AI Risks API
  slug: comp-ai-risks-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Create custom roles and resolve permission sets for organization-level access control.
  name: Comp AI Roles API
  slug: comp-ai-roles-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Create AI-powered penetration test runs, track progress, inspect findings and events, and download markdown or PDF reports.
  name: Comp AI Security Penetration Tests API
  slug: comp-ai-security-penetration-tests-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Create, auto-fill, review, approve, and export ISO 27001 Statement of Applicability documents.
  name: Comp AI SOA API
  slug: comp-ai-soa-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Create, version, run, and inspect automated evidence collection workflows attached to compliance tasks.
  name: Comp AI Task Automations API
  slug: comp-ai-task-automations-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Manage task items and attachments linked to operational entities such as risks and vendors.
  name: Comp AI Task Management API
  slug: comp-ai-task-management-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Manage compliance task lifecycle, assignments, review approvals, evidence uploads, policy links, and activity history.
  name: Comp AI Tasks API
  slug: comp-ai-tasks-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Track audit and compliance readiness timelines, phases, and review milestones for an organization.
  name: Comp AI Timelines API
  slug: comp-ai-timelines-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Record security awareness and HIPAA training completion status and generate completion certificates.
  name: Comp AI Training API
  slug: comp-ai-training-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Manage external Trust Center access requests, NDA signing, grants, tokenized document downloads, public FAQs, and reviewer access.
  name: Comp AI Trust Access API
  slug: comp-ai-trust-access-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Configure the live Trust Center, custom domain, public overview, FAQs, compliance resources, documents, links, and vendor disclosures.
  name: Comp AI Trust Portal API
  slug: comp-ai-trust-portal-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: The Uploads API from Comp AI — 1 operation(s) for uploads.
  name: Comp AI Uploads API
  slug: comp-ai-uploads-api
- baseURL: https://api.trycomp.ai
  baseurl_source: declared
  description: Manage third-party vendors, global vendor search, risk assessment triggers, and Trust Center vendor visibility.
  name: Comp AI Vendors API
  slug: comp-ai-vendors-api
artifact_total: 47
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/comp-ai/refs/heads/main/agentic-access/comp-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/comp-ai-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/comp-ai/refs/heads/main/rules/comp-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/comp-ai-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/comp-ai/refs/heads/main/json-ld/comp-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/comp-ai-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/comp-ai/refs/heads/main/vocabulary/comp-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/comp-ai-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/comp-ai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/comp-ai/refs/heads/main/data-model/comp-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/comp-ai-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.trycomp.ai/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/comp-ai/refs/heads/main/authentication/comp-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/comp-ai-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/comp-ai/refs/heads/main/errors/comp-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/comp-ai-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/comp-ai/refs/heads/main/conformance/comp-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/comp-ai-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/comp-ai/refs/heads/main/well-known/comp-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/comp-ai-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/comp-ai/refs/heads/main/hosts/comp-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/comp-ai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/comp-ai/refs/heads/main/vendors/comp-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/comp-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.trycomp.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trycomp.ai/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.trycomp.ai/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.trycomp.ai/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trust-center
- group: docs
  title: ''
  type: Documentation
  url: https://www.trycomp.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.trycomp.ai/docs/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://www.trycomp.ai/docs/integrations/oauth-setup
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/comp-ai/refs/heads/main/security/comp-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/comp-ai-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/comp-ai/refs/heads/main/security/comp-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/comp-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.trycomp.ai/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.trycomp.ai/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: Comp AI provides AI‑driven compliance automation for SOC 2, ISO 27001, HIPAA and GDPR. Their platform automates evidence collection, policy management and audit readiness, offering a dashboard, integrations with over 580 services and a security‑first architecture. Backed by a $34 M Series A, Comp AI serves fast‑growing SaaS teams to achieve compliance faster and at lower cost.
image: https://www.trycomp.ai/og.webp
json_schemas:
- name: CreateRiskDto
  property_count: 12
  slug: comp-ai-create-risk-dto
- name: CreateVendorDto
  property_count: 11
  slug: comp-ai-create-vendor-dto
- name: DeviceResponseDto
  property_count: 62
  slug: comp-ai-device-response-dto
- name: PolicyResponseDto
  property_count: 20
  slug: comp-ai-policy-response-dto
- name: UpdatePolicyDto
  property_count: 14
  slug: comp-ai-update-policy-dto
- name: UpdateRiskDto
  property_count: 12
  slug: comp-ai-update-risk-dto
jsonld:
- class_count: 120
  name: Comp Ai Context
  property_count: 249
  slug: comp-ai-context
layout: provider
modified: '2026-10-09'
name: Comp AI
nav: Providers
network: true
overview: 'Comp AI publishes 35 API contracts indexed on the [APIs.io](https://apis.io/) network, including Attachments API, Audit Logs API, Cloud Security API, and 32 more. Tagged areas include Compliance, Artificial Intelligence, SOC 2, ISO 27001, and HIPAA.


  The Comp AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Comp AI''s developer surface includes authentication, pricing, documentation, API reference, getting-started guide, and 19 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Comp AI API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: comp-ai-rules
score:
  band: developing
  composite: 47.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 35.6
    contract_quality: 61.9
    developer_ergonomics: 42.3
    discoverability: 67.9
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 35
    mcp: derived
    skills: derived
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
    score: 23.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 22.2
security:
- kind: authentication
  name: Comp Ai Authentication
  slug: comp-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Comp Ai Domain Security
  slug: comp-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Comp Ai Trust Center
  slug: comp-ai-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: comp-ai
tags:
- Compliance
- Artificial Intelligence
- SOC 2
- ISO 27001
- HIPAA
- GDPR
- Audit Automation
- Security
website: https://www.trycomp.ai/
---
