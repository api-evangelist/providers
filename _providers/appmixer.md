---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Appmixer Agentic Access
  operation_count: 33
  slug: appmixer-agentic-access
  summary_line: 33 operations · 17 acting · 1 human-in-the-loop
api_count: 12
apis:
- description: Connected third-party account management
  name: Appmixer Accounts API
  slug: appmixer-accounts-api
- description: Applications and connectors management
  name: Appmixer Apps API
  slug: appmixer-apps-api
- description: User authentication and token management
  name: Appmixer Authentication API
  slug: appmixer-authentication-api
- description: Data store management
  name: Appmixer Data Stores API
  slug: appmixer-data-stores-api
- description: File management
  name: Appmixer Files API
  slug: appmixer-files-api
- description: Workflow flow management
  name: Appmixer Flows API
  slug: appmixer-flows-api
- description: Analytics and insights
  name: Appmixer Insights API
  slug: appmixer-insights-api
- description: Flow execution logs
  name: Appmixer Logs API
  slug: appmixer-logs-api
- description: Unprocessed message management
  name: Appmixer Messages API
  slug: appmixer-messages-api
- description: Human-in-the-loop task management
  name: Appmixer People Tasks API
  slug: appmixer-people-tasks-api
- description: System health and information
  name: Appmixer System API
  slug: appmixer-system-api
- description: User account management
  name: Appmixer Users API
  slug: appmixer-users-api
arazzos:
- description: Sign a user in, confirm the session, and list their flows.
  name: Appmixer Authenticate and List Flows
  slug: appmixer-authenticate-and-list-flows-workflow
- description: Read an existing flow's definition and create a copy of it under a new name.
  name: Appmixer Clone an Existing Flow
  slug: appmixer-clone-flow-workflow
- description: Create a new flow, confirm it persisted, and start it running.
  name: Appmixer Create and Start a Flow
  slug: appmixer-create-and-start-flow-workflow
- description: Check a connected account's validity and delete it when its credentials have expired.
  name: Appmixer Disconnect an Invalid Account
  slug: appmixer-disconnect-invalid-account-workflow
- description: Create a user, authenticate to obtain a token, then create a flow for them.
  name: Appmixer Onboard a User and Create Their First Flow
  slug: appmixer-onboard-user-and-create-flow-workflow
- description: List unprocessed messages and put the first one back into the engine.
  name: Appmixer Replay an Unprocessed Message
  slug: appmixer-reprocess-unprocessed-message-workflow
- description: Stop a flow, start it again, and pull its recent execution logs.
  name: Appmixer Restart a Flow and Inspect Its Logs
  slug: appmixer-restart-flow-and-inspect-logs-workflow
- description: Read a flow, stop it if it is running, then delete it.
  name: Appmixer Decommission a Flow
  slug: appmixer-stop-and-delete-flow-workflow
- description: Read a flow, then stop it before updating if it is running, otherwise update directly.
  name: Appmixer Update a Flow Safely by Stage
  slug: appmixer-update-running-flow-workflow
artifact_total: 489
collections:
- collection_type: postman
  name: Appmixer API
  slug: postman-appmixer-api
- collection_type: open
  name: Appmixer API
  slug: open-appmixer-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/appmixer-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appmixer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/appmixer-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/appmixer/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/appmixer-authenticate-and-list-flows-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/appmixer-clone-flow-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/appmixer-create-and-start-flow-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/appmixer-disconnect-invalid-account-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/appmixer-onboard-user-and-create-flow-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/appmixer-reprocess-unprocessed-message-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/appmixer-restart-flow-and-inspect-logs-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/appmixer-stop-and-delete-flow-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/appmixer-update-running-flow-workflow.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Appmixer-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/appmixer
- group: company
  title: ''
  type: Website
  url: ''
- group: company
  title: ''
  type: Website
  url: https://www.appmixer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.appmixer.com/?_gl=1*r2dl5*_gcl_au*MTE0OTMzNzAwOC4xNzQ5MTU5NDE1*_ga*NTEwNzE5MjYuMTc0OTE1OTQxNQ..*_ga_60B263RRK5*czE3NDk1MDc4NjAkbzIkZzEkdDE3NDk1MDgzOTckajYwJGwwJGgw
- group: auth
  title: ''
  type: Authentication
  url: https://docs.appmixer.com/api/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.appmixer.com/kb
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.appmixer.com/changelog
- group: build
  title: ''
  type: SDKs
  url: https://docs.appmixer.com/6.0/6.1/getting-started/embed
- group: build
  title: ''
  type: CLI
  url: https://docs.appmixer.com/appmixer-cli/appmixer-cli?_gl=1*jj6vs6*_gcl_au*MTE0OTMzNzAwOC4xNzQ5MTU5NDE1*_ga*NTEwNzE5MjYuMTc0OTE1OTQxNQ..*_ga_60B263RRK5*czE3NDk1MDc4NjAkbzIkZzEkdDE3NDk1MDg1ODQkajMkbDAkaDA.
- group: company
  title: ''
  type: Blog
  url: https://www.appmixer.com/blog
- group: other
  title: ''
  type: Podcast
  url: https://www.appmixer.com/podcast
- group: other
  title: ''
  type: eBooks
  url: https://www.appmixer.com/e-books
- group: other
  title: ''
  type: Customers
  url: https://www.appmixer.com/customer-stories
- group: commercial
  title: ''
  type: Pricing
  url: https://www.appmixer.com/pricing
- group: auth
  title: ''
  type: Security
  url: https://www.appmixer.com/solutions-pages/cybersecurity
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.appmixer.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.appmixer.com/terms-and-conditions
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.appmixer.com/llms.txt
created: '2025-06-06T00:00:00.000Z'
description: Let your users build powerful agentic workflowsno code, fully white-labeled, and embedded right in your web app.
examples:
- key_count: 4
  name: Account Example
  slug: account-example
- key_count: 4
  name: Data Store Example
  slug: data-store-example
- key_count: 5
  name: File Example
  slug: file-example
- key_count: 4
  name: Flow Example
  slug: flow-example
- key_count: 5
  name: People Task Example
  slug: people-task-example
- key_count: 4
  name: User Example
  slug: user-example
finops:
- name: Appmixer Finops
  service_category: API
  slug: appmixer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/appmixer.png
integrations:
- name: 123FormBuilder
- name: AWS CloudWatch
- name: AWS Cloudfront
- name: AWS CodeDeploy
- name: AWS CodePipeline
- name: AWS Cognito
- name: AWS Comprehend
- name: AWS Glue
- name: AWS Kinesis
- name: AWS Lambda
- name: AWS Redshift
- name: AWS SQS
- name: AWS SageMaker
- name: AWeber
- name: Absorb
- name: Acoustic Campaign
- name: Act-On
- name: ActiveCampaign
- name: Acuity Scheduling
- name: AdRoll
- name: Adaptive Insights
- name: Adobe Experience Manager
- name: Aeries
- name: Affinity
- name: Agile CRM
- name: Ahrefs
- name: Aircall
- name: Airtable
- name: Alexa Top Sites
- name: Algolia
- name: Alteryx
- name: Amazon Athena
- name: Amazon Marketplace
- name: Amazon S3
- name: Amazon SNS
- name: Amplitude
- name: Anaplan
- name: Anthropic
- name: Apify
- name: AppNeta
- name: Appcues
- name: Appdirect ISV
- name: ArcGis
- name: Asana
- name: Atlassian Confluence
- name: Attentive Mobile
- name: Autopilot
- name: Azure Cognitive Services
- name: Azure DevOps
- name: BambooHR
- name: Base
- name: Basecamp
- name: Benchmark
- name: Bevy
- name: BigCommerce
- name: Bing Ads
- name: Bizzabo
- name: Blackboard
- name: Blueshift
- name: Boostr
- name: Box
- name: Braintree
- name: Brandfolder
- name: Braze
- name: BriteVerify
- name: Buffer
- name: Bugsnag
- name: Bynder
- name: Calendly
- name: Campaign Monitor
- name: Canvas
- name: ChannelAdvisor
- name: ChargeBee
- name: Chargeback
- name: Chargify
- name: ChartMogul
- name: ChatGPT
- name: Cisco Webex
- name: Claude
- name: Clearbit
- name: CleverReach
- name: ClickUp
- name: Close
- name: Coda
- name: ConnectWise
- name: Constant Contact
- name: Conversica
- name: ConvertKit
- name: Copper
- name: Coupa
- name: Criteo
- name: Crossbeam
- name: Cue
- name: Customer.io
- name: Cvent
- name: Databricks
- name: Datadog
- name: Datanyze
- name: DeepAI
- name: Demandbase
- name: DiscoverOrg
- name: DocRaptor
- name: Docebo
- name: DocuSign
- name: Domo
- name: Drift
- name: Dropbox
- name: ETermin
- name: Easypromos
- name: Ellucian Ethos
- name: Eloqua
- name: Emarsys
- name: Emma
- name: EventGeek
- name: Eventbrite
- name: Everhour
- name: Evernote
- name: Exchange rates
- name: Expensify
- name: ExponentHR
- name: FTP Client
- name: Facebook
- name: Fakturoid
- name: Fastpath
- name: Filemaker Pro
- name: Firebase
- name: FirstRain
- name: Fixer
- name: Float
- name: Formstack
- name: Free Forex
- name: FreshService
- name: Freshdesk
- name: Freshsales
- name: Front
- name: Frontify
- name: Fulcrum
- name: Full Contact
- name: FullStory
- name: Gainsight
- name: GetResponse
- name: Getty
- name: Giphy
- name: GitHub
- name: Gmail
- name: GoSquared
- name: GoToMeeting
- name: GoToWebinar
- name: Gong.io
- name: Google Ad Manager
- name: Google Ads
- name: Google Analytics
- name: Google BigQuery
- name: Google Calendar
- name: Google Contacts
- name: Google Drive
- name: Google Gemini
- name: Google Maps
- name: Google Search Console
- name: Google Sheets
- name: Google Slides
- name: Google Tasks
- name: Google Vision
- name: Grafana
- name: Greenbits
- name: Greenhouse
- name: Groove
- name: Groq
- name: HackerOne
- name: Harvest
- name: Hatchbuck
- name: Heap
- name: HelloSign
- name: Help Scout
- name: Highrise
- name: Hive
- name: Hootsuite
- name: Hubspot
- name: Huddle
- name: Hunter
- name: IBM DB2
- name: IBM MQ
- name: IBM Watson TTS
- name: Infusionsoft
- name: Insightly
- name: Instagram
- name: Instapage
- name: Intercom
- name: Ironclad
- name: Iterable
- name: Jasper
- name: Jenkins
- name: Jira
- name: Jive
- name: Jotform
- name: Jumio
- name: JumpCloud
- name: Kafka
- name: Kanban Tool
- name: Kapost
- name: Kazoo HR
- name: Keatext
- name: Keen
- name: Keen IO
- name: Kenshoo
- name: Kibo
- name: Kickbox
- name: Klaviyo
- name: Kochava
- name: Koncert
- name: Kudos
- name: Lattice
- name: LaunchDarkly
- name: Leadspicker
- name: LeafLink
- name: Lever
- name: Levity
- name: Lexoffice
- name: Linkedin
- name: Lithium
- name: LivePerson
- name: LiveRamp
- name: Lodash
- name: LogicMonitor
- name: Looker
- name: Mad Mimi
- name: Magento 2
- name: Mailchimp
- name: MailerLite
- name: Mailjet
- name: Mall
- name: ManagerPlus
- name: Mandrill
- name: Marketo
- name: Mattermark
- name: Merk
- name: MessageBird
- name: Microsoft Calendar
- name: Microsoft Copilot
- name: Microsoft Dynamics 365
- name: Microsoft Excel
- name: Microsoft Intune
- name: Microsoft OneDrive
- name: Microsoft Outlook
- name: Microsoft Power BI
- name: Microsoft SQL Server
- name: Microsoft Sharepoint
- name: Microsoft Teams
- name: Microsoft Text Translate
- name: Mindbody
- name: Miro
- name: Mixpanel
- name: Mode
- name: Monday
- name: MongoDB
- name: MongoDB Cloud
- name: Monkey Learn
- name: MySQL
- name: Namely
- name: Naxai
- name: New Relic
- name: NewsAPI
- name: NewsCred
- name: Nexmo
- name: Next >>
- name: Notion
- name: Noyo
- name: Okta
- name: Ollama
- name: Ometria
- name: OneLogin
- name: OneSignal
- name: Ontraport
- name: Ooma
- name: Opal
- name: OpsGenie
- name: Optimizely
- name: OptimoRoute
- name: Oracle Bronto
- name: Oracle Responsys
- name: Ordway
- name: Outreach
- name: Oxford Dictionaries
- name: PageUp
- name: PagerDuty
- name: Panaya
- name: PandaDoc
- name: Parakeet
- name: PayPal
- name: Paylocity
- name: Paymo
- name: Pendo
- name: Perplexity AI
- name: PersistIQ
- name: Personio
- name: PestRoutes
- name: Pigment
- name: Pipedrive
- name: Pipeliner
- name: PlanSource
- name: Plivo
- name: PortaBilling
- name: PortaOne
- name: PostgreSQL
- name: Postmates
- name: PowerSchool
- name: ProdPad
- name: Productboard
- name: Promoter.io
- name: Pymetrics
- name: Qualtrics
- name: Quickbase
- name: Quickbooks
- name: Raynet
- name: Recurly
- name: Redmine
- name: Rejoiner
- name: Reltio
- name: Remarkety
- name: Retention Rocket
- name: Rev.io
- name: Rho
- name: RingCentral
- name: RingRing
- name: Ringover
- name: SAP SuccessFactors
- name: SEDNA
- name: STAT
- name: Sage 300
- name: SageOne
- name: Sailthru
- name: SalesRabbit
- name: Salesforce
- name: Salesforce Marketing Cloud
- name: Salesforce Pardot
- name: SalesforceIQ
- name: Salesloft
- name: Samsara
- name: Sapling
- name: Schoology
- name: Screenshot API
- name: SearchBlox
- name: Segment
- name: Semrush
- name: SendGrid
- name: SendPulse
- name: SendinBlue
- name: Sendoso
- name: ServiceNow
- name: ServiceTitan
- name: Shopify
- name: Showpad
- name: Shutterstock
- name: Sitecore
- name: Slack
- name: SmartrMail
- name: Smartsheet
- name: Snapchat
- name: Snowflake
- name: Sparkcentral by Hootsuite
- name: Splash
- name: Square
- name: Strava
- name: Streak
- name: Stripe
- name: SugarCRM
- name: Surefire
- name: SurveySparrow
- name: Swoogo
- name: Synthesio
- name: Talkdesk
- name: Teamwork
- name: Terminus
- name: Thinkific
- name: Toggl
- name: Totango
- name: Trello
- name: Twilio
- name: Twitter
- name: Typeform
- name: Uberflip
- name: Udemy for Business
- name: UltiPro
- name: Unbounce
- name: Urban Airship
- name: User
- name: UserVoice
- name: VAT Comply
- name: VWO
- name: Vbrick
- name: Veeva
- name: Velocify
- name: VerifyEmail
- name: VerticalResponse
- name: Verve
- name: Vibes
- name: VideoAsk
- name: Virtuous CRM
- name: Virustotal
- name: Vision Critical
- name: Vonage
- name: Voys
- name: Walmart Marketplace
- name: Weather Underground
- name: Webflow
- name: WhatCounts
- name: WordPress
- name: Workable
- name: WorkflowMAX
- name: Workfront
- name: Workplace by Facebook
- name: Workstack
- name: Wrike
- name: Wufoo
- name: Wunderlist
- name: Xero
- name: Xpressdocs
- name: Xtremepush
- name: Xverify
- name: Yammer
- name: Yext
- name: Yodiz
- name: Yotpo
- name: Youtube
- name: Zaius
- name: Zendesk
- name: Zendesk Chat
- name: Zendesk Sunshine
- name: Zenefits
- name: ZeroBounce
- name: Zoho Books
- name: Zoho CRM
- name: Zoho Creator
- name: Zoom
- name: ZoomInfo
- name: Zuora
- name: dotdigital
- name: iContact
- name: iOffice
json_schemas:
- name: Appmixer Account
  property_count: 5
  slug: account
- name: Appmixer Data Store
  property_count: 2
  slug: data-store
- name: Appmixer File
  property_count: 5
  slug: file
- name: Appmixer Flow
  property_count: 8
  slug: flow
- name: Appmixer People Task
  property_count: 5
  slug: people-task
- name: Appmixer User
  property_count: 5
  slug: user
json_structures:
- name: Account Structure
  property_count: 5
  slug: account-structure
- name: Data Store Structure
  property_count: 2
  slug: data-store-structure
- name: File Structure
  property_count: 5
  slug: file-structure
- name: Flow Structure
  property_count: 8
  slug: flow-structure
- name: People Task Structure
  property_count: 5
  slug: people-task-structure
- name: User Structure
  property_count: 5
  slug: user-structure
jsonld:
- class_count: 2
  name: Appmixer Context
  property_count: 18
  slug: appmixer-context
layout: provider
modified: '2026-05-19'
name: Appmixer
nav: Providers
network: true
overview: 'Appmixer publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Apps API, Authentication API, and 9 more. Tagged areas include Agentic, Automation, Embedded iPaaS, Integrations, and Low-Code.


  The Appmixer catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Appmixer''s developer surface includes authentication, documentation, getting-started guide, changelog, CLI, engineering blog, pricing, and 24 more developer resources.'
plans:
- name: Appmixer Plans Pricing
  plan_count: 3
  slug: appmixer-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 5
  name: Appmixer Rate Limits
  slug: appmixer-rate-limits
rules:
- name: Appmixer API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: appmixer-jsonschema-spectral-rules
- name: Appmixer API Rules
  rule_count: 24
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 16
  slug: appmixer-spectral-rules
score:
  band: strong
  composite: 63.6
  delta: -3.4
  facets:
    commercial_clarity: 71.1
    contract_quality: 76.8
    developer_ergonomics: 50.0
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 63.2
  previous_composite: 67.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/appmixer/refs/heads/main/screenshots/appmixer-2026-06-20T172329.png
security:
- kind: authentication
  name: Appmixer Authentication
  slug: appmixer-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Appmixer Domain Security
  slug: appmixer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: appmixer
tags:
- Agentic
- Automation
- Embedded iPaaS
- Integrations
- Low-Code
- Workflows
---
