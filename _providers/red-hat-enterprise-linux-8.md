---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Red Hat Enterprise Linux 8 Agentic Access
  operation_count: 5
  slug: red-hat-enterprise-linux-8-agentic-access
  summary_line: 5 operations
api_count: 5
apis:
- description: Cockpit is a web-based system management interface for RHEL that exposes internal D-Bus and system APIs through a WebSocket-based transport. The Cockpit API provides access to system configuration, st
  name: RHEL 8 Cockpit Web Console API
  slug: cockpit-api
- description: RHEL System Roles are a collection of Ansible roles and modules for automating RHEL system configuration tasks including networking, storage, certificate management, SELinux, time sync, and firewall c
  name: RHEL 8 System Roles API
  slug: system-roles-api
- description: Red Hat security, bug fix, and enhancement advisories
  name: Red Hat Enterprise Linux 8 Advisories API
  slug: red-hat-enterprise-linux-8-advisories-api
- description: Common Vulnerabilities and Exposures data for Red Hat products
  name: Red Hat Enterprise Linux 8 CVEs API
  slug: red-hat-enterprise-linux-8-cves-api
- description: OVAL XML definitions for vulnerability scanning
  name: Red Hat Enterprise Linux 8 OVAL API
  slug: red-hat-enterprise-linux-8-oval-api
artifact_total: 25
collections:
- collection_type: open
  name: Red Hat Security Data API
  slug: open-red-hat-enterprise-linux-8-security-data
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/red-hat-enterprise-linux-8-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/red-hat-enterprise-linux-8-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/red-hat-enterprise-linux-8-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/red-hat-enterprise-linux-8-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://access.redhat.com/
- group: start
  title: ''
  type: Customer Portal
  url: https://console.redhat.com/
- group: docs
  title: ''
  type: Documentation
  url: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/
- group: other
  title: ''
  type: Knowledge Base
  url: https://access.redhat.com/knowledgebase/
- group: operate
  title: ''
  type: Support
  url: https://access.redhat.com/support/
- group: other
  title: ''
  type: Downloads
  url: https://access.redhat.com/downloads/
- group: company
  title: ''
  type: Blog
  url: https://www.redhat.com/en/blog/channel/red-hat-enterprise-linux
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/8.0_release_notes/index
- group: auth
  title: ''
  type: Security
  url: https://access.redhat.com/security/
- group: learn
  title: ''
  type: Training
  url: https://www.redhat.com/en/services/training-and-certification
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/redhat-developer
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.redhat.com/en/about/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.redhat.com/en/about/agreements
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/red-hat-enterprise-linux-8-security-data-openapi.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/red-hat-enterprise-linux-8-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/red-hat-enterprise-linux-8-cve-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/red-hat-enterprise-linux-8-cve-structure.json
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/red-hat-enterprise-linux-8-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/red-hat-enterprise-linux-8-vocabulary.yml
created: '2024-01-15'
description: Red Hat Enterprise Linux 8 (RHEL 8) is an enterprise-grade Linux distribution that provides a stable, secure, and high-performance operating system platform for modern IT environments. RHEL 8 is managed and accessed programmatically through Red Hat's cloud console APIs, subscription management APIs, security data APIs, and system management interfaces including Insights, Image Builder, and Cockpit. These APIs enable automated provisioning, configuration, security scanning, patch management, and compliance reporting for RHEL deployments at scale.
examples:
- key_count: 2
  name: Red Hat Enterprise Linux 8 Get Cve Example
  slug: red-hat-enterprise-linux-8-get-cve-example
- key_count: 2
  name: Red Hat Enterprise Linux 8 List Advisories Example
  slug: red-hat-enterprise-linux-8-list-advisories-example
finops:
- name: Red Hat Enterprise Linux 8 Finops
  service_category: Operating System Subscription
  slug: red-hat-enterprise-linux-8-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/red-hat-enterprise-linux-8.png
json_schemas:
- name: AdvisoryDetail
  property_count: 0
  slug: red-hat-enterprise-linux-8-advisorydetail
- name: AdvisorySummary
  property_count: 7
  slug: red-hat-enterprise-linux-8-advisorysummary
- name: Red Hat RHEL CVE
  property_count: 11
  slug: red-hat-enterprise-linux-8-cve
- name: CveDetail
  property_count: 0
  slug: red-hat-enterprise-linux-8-cvedetail
- name: CveSummary
  property_count: 7
  slug: red-hat-enterprise-linux-8-cvesummary
json_structures:
- name: Red Hat Enterprise Linux 8 Cve Structure
  property_count: 0
  slug: red-hat-enterprise-linux-8-cve-structure
- name: Red Hat Enterprise Linux 8 Structure
  property_count: 0
  slug: red-hat-enterprise-linux-8-structure
jsonld:
- class_count: 3
  name: Red Hat Enterprise Linux 8 Context
  property_count: 19
  slug: red-hat-enterprise-linux-8-context
layout: provider
modified: '2026-05-19'
name: Red Hat Enterprise Linux 8
nav: Providers
network: true
overview: 'Red Hat Enterprise Linux 8 publishes 3 APIs on the [APIs.io](https://apis.io/) network: Advisories API, CVEs API, and OVAL API. Tagged areas include Enterprise, Linux, Operating System, Red Hat, and RHEL.


  The Red Hat Enterprise Linux 8 catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Red Hat Enterprise Linux 8''s developer surface includes developer portal, documentation, support, engineering blog, release notes, training material, and 17 more developer resources.'
plans:
- name: Red Hat Enterprise Linux 8 Plans Pricing
  plan_count: 6
  slug: red-hat-enterprise-linux-8-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 1
  name: Red Hat Enterprise Linux 8 Rate Limits
  slug: red-hat-enterprise-linux-8-rate-limits
rules:
- name: Red Hat Enterprise Linux 8 API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: red-hat-enterprise-linux-8-jsonschema-spectral-rules
- name: Red Hat Enterprise Linux 8 API Rules
  rule_count: 11
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 6
  slug: red-hat-enterprise-linux-8-rules
score:
  band: developing
  composite: 55.7
  delta: -4.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 62.7
    developer_ergonomics: 23.9
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 59.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/red-hat-enterprise-linux-8/refs/heads/main/screenshots/red-hat-enterprise-linux-8-2026-06-20T192718.png
security:
- kind: domain-security
  name: Red Hat Enterprise Linux 8 Domain Security
  slug: red-hat-enterprise-linux-8-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Red Hat Enterprise Linux 8 Vulnerability Disclosure
  slug: red-hat-enterprise-linux-8-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Red Hat Enterprise Linux 8 Trust Center
  slug: red-hat-enterprise-linux-8-trust-center
  summary_line: ISO 27001, ISO 27018, HIPAA
slug: red-hat-enterprise-linux-8
tags:
- Enterprise
- Linux
- Operating System
- Red Hat
- RHEL
website: https://access.redhat.com/
---
