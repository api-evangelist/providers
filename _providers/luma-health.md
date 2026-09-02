---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 160
  human_in_the_loop: 0
  name: Luma Health Agentic Access
  operation_count: 276
  slug: luma-health-agentic-access
  summary_line: 276 operations · 160 acting
api_count: 1
apis:
- description: Patient's appointments to see a doctor
  name: Luma Health Appointments API
  slug: luma-health-appointments-api
- description: EHR appointment types
  name: Luma Health Appointment Types API
  slug: luma-health-appointmenttypes-api
- description: Audit log of individual tool calls made by the Navigator AI assistant during a conversation
  name: Luma Health Assistant Actions API
  slug: luma-health-assistantactions-api
- description: Conversations between the Navigator AI assistant and a patient or staff member
  name: Luma Health Assistant Instances API
  slug: luma-health-assistantinstances-api
- description: Transfer rules for AI assistants (Navigator) to handle call routing
  name: Luma Health Assistant Transfer Rules API
  slug: luma-health-assistanttransferrules-api
- description: Luma Client Access
  name: Luma Health Auth API
  slug: luma-health-auth-api
- description: EHR provider scheduler availability
  name: Luma Health Availabilities API
  slug: luma-health-availabilities-api
- description: Financial charges tracked against a patient, such as copays and patient balances
  name: Luma Health Billing Charges API
  slug: luma-health-billingcharges-api
- description: Copay amounts configured per source (system, EHR, or manual) and referenced by patient form templates
  name: Luma Health Billing Copays API
  slug: luma-health-billingcopays-api
- description: The Broadcast Templates API from Luma Health — 2 operation(s) for broadcast templates.
  name: Luma Health Broadcast Templates API
  slug: luma-health-broadcast-templates-api
- description: Broadcast event logs and history
  name: Luma Health Broadcast Events API
  slug: luma-health-broadcastevents-api
- description: Broadcast flows for mass messaging campaigns
  name: Luma Health Broadcast Flows API
  slug: luma-health-broadcastflows-api
- description: Contact preference campaigns that determine how and in what order a patient, facility, or user is contacted
  name: Luma Health Campaigns API
  slug: luma-health-campaigns-api
- description: conversations with a patient
  name: Luma Health Chat Activities API
  slug: luma-health-chatactivities-api
- description: reason why a chatActivity was closed
  name: Luma Health Chat Activities Reasons API
  slug: luma-health-chatactivitiesreasons-api
- description: Audits for message chat
  name: Luma Health Chat Audits API
  slug: luma-health-chataudits-api
- description: Per-appointment, per-patient instances of required pre-visit tasks generated from a checklist template
  name: Luma Health Checklists API
  slug: luma-health-checklists-api
- description: Reusable definitions of required pre-visit tasks used to build checklists
  name: Luma Health Checklist Templates API
  slug: luma-health-checklisttemplates-api
- description: custom styles, CSS, logo images for customers
  name: Luma Health Custom Web Styles API
  slug: luma-health-customwebstyles-api
- description: Append-only history of events that occurred during an engagement
  name: Luma Health Engagement Events API
  slug: luma-health-engagementevents-api
- description: Conversation sessions between the system and a recipient, driven by one or more AI agents
  name: Luma Health Engagements API
  slug: luma-health-engagements-api
- description: Reusable voice and language presets that can be attached to an engagement
  name: Luma Health Engagement Settings API
  slug: luma-health-engagementsettings-api
- description: Estimates
  name: Luma Health Estimates API
  slug: luma-health-estimates-api
- description: Customer facilities
  name: Luma Health Facilities API
  slug: luma-health-facilities-api
- description: Patient responses to NPS feedback surveys and clicks on feedback links
  name: Luma Health Feedback Responses API
  slug: luma-health-feedbackresponses-api
- description: AI-generated reply drafts for external reviews, with approve/reject workflow
  name: Luma Health Feedback Responses External Review Replies API
  slug: luma-health-feedbackresponsesexternalreviewreplies-api
- description: Scraped external reviews from Google Business Profile and Yelp
  name: Luma Health Feedback Responses External Reviews API
  slug: luma-health-feedbackresponsesexternalreviews-api
- description: Per-patient platform rotation history for NPS promoter review requests
  name: Luma Health Feedback Responses Promoter Histories API
  slug: luma-health-feedbackresponsespromoterhistories-api
- description: File Uploads
  name: Luma Health File Uploads API
  slug: luma-health-fileuploads-api
- description: Group of staff users
  name: Luma Health Groups API
  slug: luma-health-groups-api
- description: Insurance payors/carriers maintained in Luma's payor directory
  name: Luma Health Insurance Payors API
  slug: luma-health-insurancepayors-api
- description: Patient insurance coverage records
  name: Luma Health Insurances API
  slug: luma-health-insurances-api
- description: Question and answer entries for knowledge bases
  name: Luma Health Knowledge Base Question Answers API
  slug: luma-health-knowledgebasequestionanswers-api
- description: LumaBot Flows answered by patients
  name: Luma Health Lumabot Flows API
  slug: luma-health-lumabotflows-api
- description: Templates for LumaBot flows
  name: Luma Health Lumabot Flow Templates API
  slug: luma-health-lumabotflowtemplates-api
- description: Messages (chat, sms, voice, email, whatsapp, fax, in-app)
  name: Luma Health Messages API
  slug: luma-health-messages-api
- description: Reusable partials that can be composed into message templates
  name: Luma Health Message Template Partials API
  slug: luma-health-messagetemplatepartials-api
- description: Offers
  name: Luma Health Offers API
  slug: luma-health-offers-api
- description: Outbound Referral
  name: Luma Health Outbound Referrals API
  slug: luma-health-outboundreferrals-api
- description: Luma Health patient credit cards
  name: Luma Health Patient Credit Cards API
  slug: luma-health-patientcreditcards-api
- description: Patient forms answered by patients
  name: Luma Health Patient Forms API
  slug: luma-health-patientforms-api
- description: Templates from patient forms
  name: Luma Health Patient Form Templates API
  slug: luma-health-patientformtemplates-api
- description: Message templates used to compose patient communications
  name: Luma Health Patient Message Templates API
  slug: luma-health-patientmessagetemplates-api
- description: Customer patients
  name: Luma Health Patients API
  slug: luma-health-patients-api
- description: Luma Health providers
  name: Luma Health Providers API
  slug: luma-health-providers-api
- description: Groups of providers configured for shared scheduling behavior, such as round-robin or waterfall assignment
  name: Luma Health Provider Scheduling Groups API
  slug: luma-health-providerschedulinggroups-api
- description: Instances of queue manager templates representing items in a queue
  name: Luma Health Queue Manager Instances API
  slug: luma-health-queuemanagerinstances-api
- description: Recalls
  name: Luma Health Recalls API
  slug: luma-health-recalls-api
- description: Luma Patient referrals
  name: Luma Health Referrals API
  slug: luma-health-referrals-api
- description: Luma Reminders
  name: Luma Health Reminders API
  slug: luma-health-reminders-api
- description: Luma Analytical Reports
  name: Luma Health Reports API
  slug: luma-health-reports-api
- description: Scheduler
  name: Luma Health Schedulers API
  slug: luma-health-schedulers-api
- description: Luma resource settings
  name: Luma Health Settings API
  slug: luma-health-settings-api
- description: A Doctor's specialty
  name: Luma Health Specialties API
  slug: luma-health-specialties-api
- description: Messages Squigglies
  name: Luma Health Squigglies API
  slug: luma-health-squigglies-api
- description: Audit logs for certain system events in a given account
  name: Luma Health System Audits API
  slug: luma-health-systemaudits-api
- description: Staff users
  name: Luma Health Users API
  slug: luma-health-users-api
- description: Patients waiting for an appointment
  name: Luma Health Waitlists API
  slug: luma-health-waitlists-api
artifact_total: 66
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/luma-health-capability-edges.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/luma-health-manage-patient-feedback.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/luma-health-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/luma-health-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/luma-health-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/luma-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.lumahealth.io/security-and-trust/
- group: auth
  title: ''
  type: TrustCenter
  url: security/luma-health-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/luma-health-vulnerability-disclosure.yml
- group: build
  title: ''
  type: Packages
  url: packages/luma-health-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/luma-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/luma-health-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/luma-health-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/luma-health-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/luma-health-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/luma-health-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/luma-health-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/luma-health-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/luma-health-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.lumahealth.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.lumahealth.io
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.lumahealth.io
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.lumahealth.io
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/luma-health-openapi.yaml
- group: company
  title: ''
  type: Blog
  url: https://www.lumahealth.io/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.lumahealth.io/blog/feed/
- group: learn
  title: ''
  type: Learn
  url: https://www.lumahealth.io/learn
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.lumahealth.io/hc/en-us
- group: company
  title: ''
  type: Newsroom
  url: https://www.lumahealth.io/newsroom/in-the-news/
- group: company
  title: ''
  type: Careers
  url: https://job-boards.greenhouse.io/lumahealth
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lumahealth.io
- group: auth
  title: ''
  type: Security
  url: security/luma-health-vulnerability-disclosure.yml
- group: start
  title: ''
  type: Login
  url: https://next.lumahealth.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lumahealth.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lumahealth.io/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lumahealthhq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/luma-health
created: '2026-07-24'
description: Luma Health is a United States patient-engagement (Patient Success) platform for healthcare provider organizations, headquartered in San Francisco, California. Its operational AI platform automates the patient journey - self-service scheduling and appointment management, referral and waitlist management, intake and digital forms, omnichannel two-way messaging and broadcast, appointment reminders and recalls, insurance eligibility verification, payments and billing, and a conversational AI assistant (Navigator / lumabot) - and integrates bidirectionally with the major EHRs (Epic, Oracle Health/Cerner, MEDITECH, eClinicalWorks, athenahealth, NextGen, Greenway, Nextech). Luma exposes a documented public REST API (Rest-Service v2.0.0, OpenAPI 3.0.0) at https://api.lumahealth.io/api/v2, secured with OAuth2 client-credentials that issue JWT bearer tokens. The developer-facing surface is a REST API rather than an HL7 FHIR server; FHIR/HL7 interoperability with EHRs happens inside Luma's
  integration layer, not as a public FHIR endpoint.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Luma Health MCP Server
  slug: luma-health-mcp-server
modified: '2026-08-15'
name: Luma Health
nav: Providers
network: true
overview: 'Luma Health publishes 58 APIs on the [APIs.io](https://apis.io/) network, including Appointments API, Appointment Types API, Assistant Actions API, and 55 more. Tagged areas include Healthcare, United States, Patient Engagement, Scheduling, and Referrals.


  Luma Health''s developer surface includes authentication, documentation, API reference, engineering blog, and 34 more developer resources.'
plans:
- name: Luma Health Plans Pricing
  plan_count: 0
  slug: luma-health-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Luma Health Rate Limits
  slug: luma-health-rate-limits
score:
  band: developing
  composite: 45.8
  coverage:
    artifact_dirs: 20
    catalog_gap: 81.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 4.5
    contract_quality: 54.6
    developer_ergonomics: 36.3
    discoverability: 70.4
    governance: 4.5
    operational_transparency: 28.9
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 58
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 51.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/luma-health/refs/heads/main/screenshots/luma-health-2026-07-25T225704.png
security:
- kind: authentication
  name: Luma Health Authentication
  slug: luma-health-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Luma Health Domain Security
  slug: luma-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Luma Health Vulnerability Disclosure
  slug: luma-health-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Luma Health Trust Center
  slug: luma-health-trust-center
  summary_line: HITRUST CSF r2, SOC 2 Type II, ISO/IEC 27001:2022, ISO/IEC 42001 (AI management system, for Luma AI products), HIPAA, TX-RAMP Level 2, EU-US Data Privacy Framework (with UK and Swiss extensions)
slug: luma-health
tags:
- Healthcare
- United States
- Patient Engagement
- Scheduling
- Referrals
- Intake
- Messaging
- Eligibility
- EHR
- Interoperability
- Clinical AI
- Reputation Management
- Patient Feedback
website: https://www.lumahealth.io
---
