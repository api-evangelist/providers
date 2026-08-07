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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Axonius is a cybersecurity asset management platform providing SaaS management, device discovery, and security policy enforcement across IT environments.
  name: Axonius
  slug: axonius
artifact_total: 24
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/axonius-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/axonius-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/axonius
- group: company
  title: ''
  type: Website
  url: https://www.axonius.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.axonius.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Axonius
- group: company
  title: ''
  type: Blog
  url: https://www.axonius.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.axonius.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.axonius.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.axonius.com/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.axonius.com/docs/getting-started
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.axonius.com/llms.txt
created: '2026-03-27'
description: Axonius is a cybersecurity asset management platform providing SaaS management, device discovery, and security policy enforcement across IT environments.
features:
- description: Automatically discover all devices, users, and cloud assets across the environment.
  name: Asset Discovery
- description: Manage SaaS application access, licenses, and security posture from a single platform.
  name: SaaS Management
- description: Enforce security policies across assets and trigger automated remediation workflows.
  name: Security Enforcement
- description: Connect to 800+ security and IT tools for data aggregation and correlation.
  name: Integration Hub
- description: Correlate vulnerability scanner data with asset context for prioritized remediation.
  name: Vulnerability Management
- description: Generate compliance reports for CIS Benchmarks, NIST, PCI DSS, and other frameworks.
  name: Compliance Reporting
- description: Build complex queries to find assets matching specific security criteria.
  name: Query Builder
- description: Track asset lifecycle from procurement to decommission with full audit trail.
  name: Lifecycle Management
finops:
- name: Axonius Finops
  service_category: API
  slug: axonius-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/axonius.png
integrations:
- description: Pull endpoint data from CrowdStrike Falcon to enrich asset inventory.
  name: CrowdStrike
- description: Sync user and device data from Active Directory and Azure AD.
  name: Microsoft Active Directory
- description: Push asset data and incidents to ServiceNow CMDB and ITSM.
  name: ServiceNow
- description: Correlate Qualys vulnerability scan data with asset context.
  name: Qualys
- description: Correlate SaaS user access data with identity from Okta.
  name: Okta
layout: provider
modified: '2026-04-19'
name: Axonius
nav: Providers
network: true
overview: 'Axonius publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Asset Management, Cybersecurity, SaaS Management, and SaaS Security.


  Axonius'' developer surface includes documentation, engineering blog, pricing, getting-started guide, and 8 more developer resources.'
plans:
- name: Axonius Plans Pricing
  plan_count: 3
  slug: axonius-plans-pricing
random_paper: 97
rate_limits:
- limit_count: 5
  name: Axonius Rate Limits
  slug: axonius-rate-limits
score:
  band: thin
  composite: 29.0
  delta: 0.0
  facets:
    commercial_clarity: 78.9
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 29.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/axonius/refs/heads/main/screenshots/axonius-2026-06-20T172834.png
security:
- kind: domain-security
  name: Axonius Domain Security
  slug: axonius-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Axonius Trust Center
  slug: axonius-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, FedRAMP, CSA STAR
slug: axonius
tags:
- Asset Management
- Cybersecurity
- SaaS Management
- SaaS Security
use_cases:
- description: Maintain a complete, always-accurate inventory of all IT and OT assets.
  name: Asset Inventory
- description: Identify unauthorized devices and SaaS applications in use across the organization.
  name: Shadow IT Discovery
- description: Enforce zero trust policies by continuously validating asset compliance.
  name: Zero Trust Security
- description: Quickly identify affected assets during security incidents for rapid containment.
  name: Incident Response
- description: Prove compliance with security frameworks using comprehensive asset data.
  name: Compliance Auditing
website: https://www.axonius.com
---
