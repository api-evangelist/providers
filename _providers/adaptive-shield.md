---
access_model:
  confidence: high
  label: Contact sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans/adaptive-shield-plans-pricing.yml
  - https://www.crowdstrike.com/en-us/pricing/
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'The Adaptive Shield REST API v1 provides programmatic access to SaaS security posture data including alerts, user and device inventory, integration configurations, security check results, violations, '
  name: Adaptive Shield REST API
  slug: adaptive-shield-api
artifact_total: 28
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/adaptive-shield-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/adaptive-shield-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adaptive-shield-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adaptiveshield
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adaptiveshield
- group: company
  title: ''
  type: Website
  url: https://www.crowdstrike.com/en-us/platform/falcon-shield/
- group: start
  title: ''
  type: Portal
  url: https://www.crowdstrike.com/en-us/platform/falcon-shield/
- group: company
  title: ''
  type: Blog
  url: https://www.crowdstrike.com/en-us/blog/
- group: other
  title: ''
  type: Resources
  url: https://www.crowdstrike.com/en-us/resources/
- group: operate
  title: ''
  type: Support
  url: https://supportportal.crowdstrike.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/adaptive-shield-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/adaptive-shield-security.txt
- group: auth
  title: ''
  type: Security
  url: security/adaptive-shield-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: security/adaptive-shield-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adaptive-shield-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/adaptive-shield-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adaptive-shield-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/adaptive-shield-plans-pricing.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.crowdstrike.com/en-us/legal/privacy-notice/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.crowdstrike.com/en-us/legal/terms-conditions/
created: '2026-03-27'
description: Adaptive Shield (now CrowdStrike Falcon Shield) is a SaaS Security Posture Management (SSPM) platform that continuously monitors, remediates, and governs SaaS application security configurations and identity risks. Acquired by CrowdStrike, the platform covers 200+ SaaS integrations with over 3,500 built-in security checks, helping organizations detect misconfigurations, manage human and non-human identities, discover shadow applications, and maintain compliance across their entire SaaS stack. The REST API (v1) enables programmatic access to alerts, user inventory, device inventory, integrations, security checks, and compliance data.
features:
- description: Continuously monitors 200+ SaaS applications with 3,500+ built-in security checks to detect and remediate misconfigurations that expose organizations to security risks.
  name: SaaS Misconfiguration Detection
- description: Manages both human and non-human identities (NHI) across SaaS platforms, detecting over-privileged accounts and suspicious access patterns.
  name: Identity And Access Governance
- description: Discovers unsanctioned and shadow SaaS applications connected to the organization's environment, providing visibility into unauthorized integrations.
  name: Shadow App Discovery
- description: Provides visibility into and governance over AI agents operating within enterprise SaaS platforms including Microsoft 365, Salesforce, and OpenAI.
  name: AI Agent Visibility And Control
- description: Tracks compliance posture across SaaS applications against frameworks such as SOC 2, ISO 27001, GDPR, and HIPAA using automated security check mappings.
  name: Compliance Monitoring
- description: Public REST API v1 with API key authentication enables programmatic access to alerts, user/device inventory, integration data, security check results, violations, and compliance controls. US and EU regional endpoints available.
  name: REST API Access
- description: Integrates with SIEM platforms (Splunk, Datadog), security platforms (CrowdStrike Falcon), and vulnerability management platforms via API and native connectors.
  name: SIEM And Platform Integrations
finops:
- name: Adaptive Shield Finops
  service_category: API
  slug: adaptive-shield-finops
image: /assets/icons/adaptive-shield.png
integrations:
- description: SaaS security monitoring for Microsoft 365 suite including Exchange, Teams, SharePoint, and OneDrive.
  name: Microsoft 365
- description: Security posture monitoring and misconfiguration detection for Salesforce CRM.
  name: Salesforce
- description: Configuration monitoring and security checks for Slack workspace settings.
  name: Slack
- description: Security configuration monitoring for Zoom video conferencing accounts.
  name: Zoom
- description: Identity provider integration for user access and authentication configuration monitoring.
  name: Okta
- description: Sends SaaS posture alerts as Datadog Events via OAuth integration.
  name: Datadog
- description: Splunk add-on for ingesting Adaptive Shield security events and alerts.
  name: Splunk
- description: Native integration with CrowdStrike Falcon platform following acquisition.
  name: CrowdStrike Falcon
layout: provider
modified: '2026-08-30'
name: Adaptive Shield
nav: Providers
network: true
overview: 'Adaptive Shield publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include SaaS Security, SSPM, Security Posture Management, Cybersecurity, and Cloud Security.


  Adaptive Shield''s developer surface includes developer portal, engineering blog, support, and 17 more developer resources.'
plans:
- name: Adaptive Shield Plans Pricing
  plan_count: 0
  slug: adaptive-shield-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Adaptive Shield Rate Limits
  slug: adaptive-shield-rate-limits
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 27.2
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adaptive-shield/refs/heads/main/screenshots/adaptive-shield-2026-06-20T164619.png
security:
- kind: authentication
  name: Adaptive Shield Authentication
  slug: adaptive-shield-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Adaptive Shield Domain Security
  slug: adaptive-shield-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Adaptive Shield Vulnerability Disclosure
  slug: adaptive-shield-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Adaptive Shield Trust Center
  slug: adaptive-shield-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, PCI DSS, FedRAMP, GDPR, CSA STAR
slug: adaptive-shield
tags:
- SaaS Security
- SSPM
- Security Posture Management
- Cybersecurity
- Cloud Security
- Identity Management
- Compliance
use_cases:
- description: Security teams can continuously monitor and remediate misconfigurations across the organization's entire SaaS stack from a single dashboard.
  name: SaaS Security Posture Management
- description: Detect and remediate over-privileged users, dormant accounts, and suspicious login behavior across all connected SaaS applications.
  name: Identity Risk Detection
- description: Automate compliance evidence collection and posture monitoring for SOC 2, ISO 27001, GDPR, and other frameworks across SaaS applications.
  name: Compliance Audit Automation
- description: Identify and assess risk from third-party OAuth apps and browser extensions connected to critical SaaS platforms.
  name: Third-Party App Risk Management
- description: Pull SaaS security alerts and posture data into SIEM and SOAR platforms via the REST API for unified security operations workflows.
  name: Security Operations Integration
website: https://www.crowdstrike.com/en-us/platform/falcon-shield/
---
