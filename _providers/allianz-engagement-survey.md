---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
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
  schema_version: 0.2
  score: 30.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Allianz Engagement Survey Agentic Access
  operation_count: 9
  slug: allianz-engagement-survey-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 5
apis:
- description: Action plan tracking and management operations
  name: Allianz Engagement Survey Action Plans API
  slug: allianz-engagement-survey-action-plans-api
- description: Survey analytics, reporting, and insights operations
  name: Allianz Engagement Survey Analytics API
  slug: allianz-engagement-survey-analytics-api
- description: Survey participant and invitation management operations
  name: Allianz Engagement Survey Participants API
  slug: allianz-engagement-survey-participants-api
- description: Survey response submission and retrieval operations
  name: Allianz Engagement Survey Responses API
  slug: allianz-engagement-survey-responses-api
- description: Survey lifecycle management operations
  name: Allianz Engagement Survey Surveys API
  slug: allianz-engagement-survey-surveys-api
artifact_total: 77
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Allianz Engagement Survey Action Plans API
  slug: open-allianz-engagement-survey-action-plans-api
- collection_type: open
  name: Allianz Engagement Survey Action Plans Analytics API
  slug: open-allianz-engagement-survey-analytics-api
- collection_type: open
  name: Allianz Engagement Survey Action Plans Participants API
  slug: open-allianz-engagement-survey-participants-api
- collection_type: open
  name: Allianz Engagement Survey Action Plans Responses API
  slug: open-allianz-engagement-survey-responses-api
- collection_type: open
  name: Allianz Engagement Survey Action Plans Surveys API
  slug: open-allianz-engagement-survey-surveys-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/allianz-engagement-survey-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/allianz-engagement-survey-engagement-survey-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/allianz-engagement-survey-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/allianz-engagement-survey-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/allianz-engagement-survey-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/allianz-engagement-survey-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.allianz.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/allianz
- group: design
  title: ''
  type: SpectralRules
  url: rules/allianz-engagement-survey-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/allianz-engagement-survey-vocabulary.yaml
- group: company
  title: ''
  type: Blog
  url: https://www.allianz.com/en/press.html
- group: build
  title: ''
  type: Packages
  url: packages/allianz-engagement-survey-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/allianz-engagement-survey-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/allianz-engagement-survey-llms.txt
created: '2024-01-15'
description: The Allianz Engagement Survey API enables management of employee engagement surveys across the Allianz organization. It provides capabilities for survey lifecycle management, participant management, response collection, and analytics reporting to support Allianz's global employee experience initiatives.
examples:
- key_count: 8
  name: Engagement Survey Action Plan Example
  slug: engagement-survey-action-plan-example
- key_count: 2
  name: Engagement Survey Action Plan List Example
  slug: engagement-survey-action-plan-list-example
- key_count: 2
  name: Engagement Survey Add Participants Request Example
  slug: engagement-survey-add-participants-request-example
- key_count: 3
  name: Engagement Survey Add Participants Response Example
  slug: engagement-survey-add-participants-response-example
- key_count: 3
  name: Engagement Survey Answer Example
  slug: engagement-survey-answer-example
- key_count: 4
  name: Engagement Survey Create Action Plan Request Example
  slug: engagement-survey-create-action-plan-request-example
- key_count: 5
  name: Engagement Survey Create Survey Request Example
  slug: engagement-survey-create-survey-request-example
- key_count: 5
  name: Engagement Survey Participant Example
  slug: engagement-survey-participant-example
- key_count: 4
  name: Engagement Survey Participant List Example
  slug: engagement-survey-participant-list-example
- key_count: 4
  name: Engagement Survey Question Score Example
  slug: engagement-survey-question-score-example
- key_count: 2
  name: Engagement Survey Response List Example
  slug: engagement-survey-response-list-example
- key_count: 5
  name: Engagement Survey Survey Analytics Example
  slug: engagement-survey-survey-analytics-example
- key_count: 9
  name: Engagement Survey Survey Example
  slug: engagement-survey-survey-example
- key_count: 4
  name: Engagement Survey Survey List Example
  slug: engagement-survey-survey-list-example
- key_count: 4
  name: Engagement Survey Survey Response Example
  slug: engagement-survey-survey-response-example
features:
- description: Create, configure, publish, and close employee engagement surveys with full lifecycle tracking and audit capabilities.
  name: Survey Lifecycle Management
- description: Manage survey participants, send invitations, track response rates, and send reminders to boost participation across business units.
  name: Participant Management
- description: Collect structured survey responses with support for multiple question types including Likert scales, open text, and multiple choice.
  name: Response Collection
- description: Generate engagement analytics, participation metrics, and comparative reports across departments, regions, and time periods.
  name: Analytics and Reporting
- description: Segment survey results by business unit, geography, role, tenure, and demographic dimensions for targeted insights.
  name: Segmentation
- description: Track and manage action plans created in response to survey insights to drive employee experience improvements.
  name: Action Planning
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/allianz-engagement-survey.png
integrations:
- description: Integration with Workday HCM for automated participant roster management and organizational hierarchy synchronization.
  name: Workday
- description: Survey notifications and reminders delivered through Microsoft Teams to increase employee participation rates.
  name: Microsoft Teams
- description: Export engagement analytics to Power BI for advanced visualization and executive dashboard reporting.
  name: Power BI
json_schemas:
- name: ActionPlanList
  property_count: 2
  slug: engagement-survey-action-plan-list
- name: ActionPlan
  property_count: 8
  slug: engagement-survey-action-plan
- name: AddParticipantsRequest
  property_count: 2
  slug: engagement-survey-add-participants-request
- name: AddParticipantsResponse
  property_count: 3
  slug: engagement-survey-add-participants-response
- name: Answer
  property_count: 3
  slug: engagement-survey-answer
- name: CreateActionPlanRequest
  property_count: 4
  slug: engagement-survey-create-action-plan-request
- name: CreateSurveyRequest
  property_count: 5
  slug: engagement-survey-create-survey-request
- name: ParticipantList
  property_count: 4
  slug: engagement-survey-participant-list
- name: Participant
  property_count: 5
  slug: engagement-survey-participant
- name: QuestionScore
  property_count: 4
  slug: engagement-survey-question-score
- name: ResponseList
  property_count: 2
  slug: engagement-survey-response-list
- name: SurveyAnalytics
  property_count: 5
  slug: engagement-survey-survey-analytics
- name: SurveyList
  property_count: 4
  slug: engagement-survey-survey-list
- name: SurveyResponse
  property_count: 4
  slug: engagement-survey-survey-response
- name: Survey
  property_count: 9
  slug: engagement-survey-survey
json_structures:
- name: Engagement Survey Action Plan List Structure
  property_count: 2
  slug: engagement-survey-action-plan-list-structure
- name: Engagement Survey Action Plan Structure
  property_count: 8
  slug: engagement-survey-action-plan-structure
- name: Engagement Survey Add Participants Request Structure
  property_count: 2
  slug: engagement-survey-add-participants-request-structure
- name: Engagement Survey Add Participants Response Structure
  property_count: 3
  slug: engagement-survey-add-participants-response-structure
- name: Engagement Survey Answer Structure
  property_count: 3
  slug: engagement-survey-answer-structure
- name: Engagement Survey Create Action Plan Request Structure
  property_count: 4
  slug: engagement-survey-create-action-plan-request-structure
- name: Engagement Survey Create Survey Request Structure
  property_count: 5
  slug: engagement-survey-create-survey-request-structure
- name: Engagement Survey Participant List Structure
  property_count: 4
  slug: engagement-survey-participant-list-structure
- name: Engagement Survey Participant Structure
  property_count: 5
  slug: engagement-survey-participant-structure
- name: Engagement Survey Question Score Structure
  property_count: 4
  slug: engagement-survey-question-score-structure
- name: Engagement Survey Response List Structure
  property_count: 2
  slug: engagement-survey-response-list-structure
- name: Engagement Survey Survey Analytics Structure
  property_count: 5
  slug: engagement-survey-survey-analytics-structure
- name: Engagement Survey Survey List Structure
  property_count: 4
  slug: engagement-survey-survey-list-structure
- name: Engagement Survey Survey Response Structure
  property_count: 4
  slug: engagement-survey-survey-response-structure
- name: Engagement Survey Survey Structure
  property_count: 9
  slug: engagement-survey-survey-structure
jsonld:
- class_count: 16
  name: Allianz Engagement Survey Context
  property_count: 38
  slug: allianz-engagement-survey-context
layout: provider
mcp_servers:
- description: ''
  name: Allianz Engagement Survey MCP Server
  slug: allianz-engagement-survey-mcp-server
modified: '2026-06-20'
name: Allianz Engagement Survey
nav: Providers
network: true
overview: 'Allianz Engagement Survey publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Action Plans API, Analytics API, Participants API, and 2 more. Tagged areas include Analytics, Enterprise, Human Resources, Insurance, and Surveys.


  The Allianz Engagement Survey catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Allianz Engagement Survey''s developer surface includes authentication, engineering blog, and 12 more developer resources.'
random_paper: 12
rules:
- effective_rule_count: 5
  extends: []
  name: Allianz Engagement Survey API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: allianz-engagement-survey-jsonschema-spectral-rules
- effective_rule_count: 73
  extends:
  - spectral:oas
  name: Allianz Engagement Survey API Rules
  rule_count: 32
  severity_counts:
    error: 15
    hint: 0
    info: 2
    warn: 15
  slug: allianz-engagement-survey-spectral-rules
scopes:
- name: Allianz Engagement Survey Scopes
  scope_count: 5
  slug: allianz-engagement-survey-scopes
  summary_line: 5 scopes · clientCredentials
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 22
    catalog_gap: 48.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 33.3
    contract_quality: 29.4
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 33.3
    operational_transparency: 5.3
  previous_composite: 27.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 51.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/allianz-engagement-survey/refs/heads/main/screenshots/allianz-engagement-survey-2026-07-25T195701.png
security:
- kind: authentication
  name: Allianz Engagement Survey Authentication
  slug: allianz-engagement-survey-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Allianz Engagement Survey Domain Security
  slug: allianz-engagement-survey-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: allianz-engagement-survey
tags:
- Analytics
- Enterprise
- Human Resources
- Insurance
- Surveys
- Employee Experience
use_cases:
- description: Run company-wide annual employee engagement surveys to measure satisfaction, commitment, and advocacy across all Allianz entities.
  name: Annual Engagement Survey
- description: Deploy frequent short pulse surveys to track engagement trends and respond quickly to changing employee sentiment.
  name: Pulse Surveys
- description: Capture new employee experience feedback during onboarding to improve the joining experience and early retention.
  name: Onboarding Surveys
- description: Collect departing employee feedback to understand attrition drivers and improve retention strategies.
  name: Exit Surveys
website: https://www.allianz.com/
---
