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
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Cobalt Agentic Access
  operation_count: 31
  slug: cobalt-agentic-access
  summary_line: 31 operations · 17 acting
api_count: 10
apis:
- description: Retrieve details about enabled applications.
  name: Cobalt Applications API
  slug: cobalt-applications-api
- description: Generate hosted portal URLs for linked accounts.
  name: Cobalt Cobalt Hosted API
  slug: cobalt-cobalt-hosted-api
- description: Manage integration configurations for linked accounts.
  name: Cobalt Config API
  slug: cobalt-config-api
- description: Manage datastores and their records.
  name: Cobalt Datastores API
  slug: cobalt-datastores-api
- description: Trigger events to initiate workflows.
  name: Cobalt Events API
  slug: cobalt-events-api
- description: Retrieve details about workflow executions.
  name: Cobalt Executions API
  slug: cobalt-executions-api
- description: Manage linked accounts representing your end-customers.
  name: Cobalt Linked Accounts API
  slug: cobalt-linked-accounts-api
- description: Create and manage public workflows.
  name: Cobalt Public Workflows API
  slug: cobalt-public-workflows-api
- description: Generate session tokens for linked account authentication.
  name: Cobalt Session Token API
  slug: cobalt-session-token-api
- description: Subscribe to real-time notifications when events occur in Cobalt.
  name: Cobalt Webhooks API
  slug: cobalt-webhooks-api
artifact_total: 1114
collections:
- collection_type: postman
  name: Cobalt Applications API
  slug: postman-cobalt-applications-api
- collection_type: postman
  name: Cobalt Applications Cobalt Hosted API
  slug: postman-cobalt-cobalt-hosted-api
- collection_type: postman
  name: Cobalt Applications Config API
  slug: postman-cobalt-config-api
- collection_type: postman
  name: Cobalt Applications Datastores API
  slug: postman-cobalt-datastores-api
- collection_type: postman
  name: Cobalt Applications Events API
  slug: postman-cobalt-events-api
- collection_type: postman
  name: Cobalt Applications Executions API
  slug: postman-cobalt-executions-api
- collection_type: postman
  name: Cobalt Applications Linked Accounts API
  slug: postman-cobalt-linked-accounts-api
- collection_type: postman
  name: Cobalt Applications Public Workflows API
  slug: postman-cobalt-public-workflows-api
- collection_type: postman
  name: Cobalt Applications Session Token API
  slug: postman-cobalt-session-token-api
- collection_type: postman
  name: Cobalt Applications Webhooks API
  slug: postman-cobalt-webhooks-api
- collection_type: open
  name: Cobalt API
  slug: open-cobalt-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/cobalt/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cobalt-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cobalt-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cobalt-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cobalt-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cobalthq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cobalt_io
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/cobalt-api-openapi.yml
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/cobalt-rules.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/cobalt-context.jsonld
- group: company
  title: ''
  type: About
  url: https://www.gocobalt.io/about-us
- group: company
  title: ''
  type: Website
  url: https://www.gocobalt.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.gocobalt.io/overview
- group: design
  title: ''
  type: Workflow
  url: https://docs.gocobalt.io/build/workflow/overview
- group: auth
  title: ''
  type: Security
  url: https://docs.gocobalt.io/governance/overview
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.gocobalt.io/governance/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.gocobalt.io/governance/terms-of-use
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gocobalt.io/api-reference/overview
- group: build
  title: ''
  type: SDKs
  url: https://docs.gocobalt.io/sdks/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gocobalt.io/pricing
- group: auth
  title: ''
  type: Security
  url: https://www.gocobalt.io/security
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gocobalt.io/status/app
- group: start
  title: ''
  type: Signup
  url: https://www.gocobalt.io/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.gocobalt.io/login
- group: company
  title: ''
  type: Blog
  url: https://www.gocobalt.io/blog/feed
created: '2025-06-05'
description: Traditional integrations are slow, fragmented, and hinder growth. Cobalt is changing that. A next-gen integration platform with 1,000+ connectors and AI-driven automation redefining how businesses integrate, operate, and scale.
features:
- name: Advanced Observability
- name: Advanced Uptime Slas
- name: AI Integration Agents
- name: Custom App Builder With AI
- name: Customer-Facing Workflows
- name: Deployment in Your VPC
- name: Dynamic Field Mapping
- name: End-Customer Cloud Deployment
- name: End-Customer On-Premise
- name: Everything in Cloud Plus
- name: Integration Solutioning
- name: Logs Streaming via API
- name: Multi-Region Deployment
- name: Option for Dedicated Cluster
- name: Priority Support
- name: Production Tenants
- name: Red-Badge Engineers
- name: Saml-Based SSO
- name: Slack Teams Onboarding
- name: Syncing & Polling
- name: Unlimited API Calls
- name: Unlimited Tenants
- name: Unlimited Connectors
- name: Unlimited Workflows
- name: Whiteglove Support
finops:
- name: Cobalt Finops
  service_category: API
  slug: cobalt-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cobalt.png
integrations:
- name: 0codekit
- name: 15Five
- name: 1C
- name: 1CRM
- name: 1Password
- name: 1msg
- name: 247.ai
- name: 2Checkout
- name: 3dcart
- name: 42Crunch
- name: 500apps
- name: 6sense
- name: 7shifts
- name: 8x8
- name: A/B Tasty
- name: ACI PAY.ON
- name: ADP
- name: AMcards
- name: AWS Cognito
- name: AWS Lambda
- name: AWS SNS
- name: AWS SQS
- name: AWS Secrets Manager
- name: AWS Security Hub
- name: Ably
- name: Accelo
- name: Accengage
- name: Acquia
- name: Actblue
- name: Actian
- name: Action Builder
- name: Active Campaign
- name: ActiveProspect
- name: Acuant
- name: Acuity Scheduling
- name: Acumatica
- name: Acunetix
- name: AdRoll
- name: Addevent
- name: Adobe Analytics
- name: Adobe Commerce
- name: Adobe Experience Manager
- name: Adobe PDF Services
- name: Adobe Sign
- name: Adobe Workfront
- name: Adyen
- name: AeroLeads
- name: Affinity
- name: AfterShip
- name: Agenty
- name: Agile CRM
- name: Agiloft
- name: Agora
- name: Aha!
- name: Ahrefs
- name: AirOps
- name: Airbyte
- name: Aircall
- name: Airmeet
- name: Airship
- name: Airslate
- name: Airtable
- name: Aiven
- name: Akamai
- name: Akeneo
- name: Albato
- name: Alegra
- name: Alert Logic
- name: Algolia Search
- name: Algorand
- name: Alibaba Cloud
- name: Alight Solutions
- name: AlphaSense
- name: Amadeus
- name: Amazon API Gateway
- name: Amazon Advertising
- name: Amazon Athena
- name: Amazon Cognito
- name: Amazon DynamoDB
- name: Amazon ECS
- name: Amazon EKS
- name: Amazon Elasticsearch
- name: Amazon EventBridge
- name: Amazon Location Service
- name: Amazon Polly
- name: Amazon Redshift
- name: Amazon S3
- name: Amazon SES
- name: Amazon SageMaker
- name: Amazon Seller Central
- name: Ambassador Edge Stack
- name: Ambivo
- name: AmoCRM
- name: Amplitude
- name: Anaplan
- name: Anodot
- name: Ansible
- name: Anthropic Claude
- name: Apache Spark
- name: Apollo.io
- name: AppDirect
- name: Applitools
- name: ApprovalMax
- name: Appsmith
- name: Apptivo CRM
- name: Apttus
- name: ArangoDB
- name: Armory.io
- name: Asana
- name: Ascent Erp
- name: Ashby
- name: AskNicely
- name: Astra Security
- name: Astronaut
- name: Asure Software
- name: Athenahealth
- name: Attio
- name: Auth0
- name: Autodesk BIM 360
- name: Autodesk Revit
- name: Automox
- name: Avalara
- name: Avaloq
- name: Aweber
- name: Azure AI Vision
- name: Azure API Management
- name: Azure Blob Storage
- name: Azure DevOps
- name: Azure Key Vault
- name: Azure OpenAI Service
- name: Azure Security Center
- name: Azure Speech Service
- name: Backblaze
- name: Backlog
- name: BambooHR
- name: Bambora
- name: Bannerbear
- name: Baremetrics
- name: Basecamp
- name: Beanstalk Payment Technologies
- name: Beehiiv
- name: Better Proposals
- name: Bexio
- name: BigCommerce
- name: BigID
- name: BigML
- name: Bigtincan
- name: Bill
- name: Birdeye
- name: BitBucket
- name: Bitrise
- name: Bitwarden
- name: BloomReach
- name: Bluebeam
- name: Bolt
- name: Bombora
- name: Bot9
- name: Box
- name: Braintree
- name: Branch
- name: Brandfolder
- name: Braze
- name: Breezy HR
- name: Brevo (Sendinblue)
- name: Brex
- name: BrightAnalytics
- name: BrightPay UK
- name: Brightcove
- name: Bringg
- name: Broadridge
- name: Browse AI
- name: BrowserStack
- name: Bugsnag
- name: Bugzilla
- name: BuiltWith
- name: Burp Suite
- name: CData Software
- name: Cal.com
- name: Calendly
- name: CallPage
- name: Campaign Monitor
- name: Canny
- name: Canva
- name: Capsule CRM
- name: Carto
- name: Cashfree
- name: Caspio
- name: Catalyst
- name: Ceipal
- name: Celigo
- name: Celonis
- name: CentralStationCRM
- name: Ceridian Dayforce
- name: Certify
- name: Chargebee
- name: Chargent
- name: Checkmarx
- name: Checkout.com
- name: Checkr
- name: Chef
- name: Chili Piper
- name: Chorus
- name: ChurnZero
- name: Circle
- name: Cisco Duo
- name: Cisco Meraki
- name: Cisco Spark
- name: Citrix
- name: CiviCRM
- name: Clari Copilot
- name: Clear Books
- name: Clear Software
- name: Clearbit
- name: Clerk.io
- name: CleverTap
- name: ClickFunnels
- name: ClickMeter
- name: ClickSend SMS
- name: ClickUp
- name: ClinchPad
- name: Clio Manage
- name: Close CRM
- name: Cloud Firestore
- name: Cloud Watch
- name: Cloudflare
- name: Cloudflare API Shield
- name: Cloudflare R2
- name: Cloudflare Workers
- name: Cloudinary
- name: Clover
- name: CockroachDB
- name: Coda
- name: Codat
- name: Code42
- name: Cognite
- name: Cognito
- name: Cohere
- name: Collibra
- name: CommandBar
- name: Commercetools
- name: Common Paper
- name: Confluence
- name: Constant Contact
- name: Contentful
- name: Contractbook
- name: Contrast Security
- name: Convoy
- name: Copper
- name: Cordial
- name: Couchbase
- name: Coupa
- name: Coupa Pay
- name: Cradlepoint
- name: Criteo
- name: Cross River
- name: CrowdStrike
- name: Customer.io
- name: CyberArk
- name: D2L Brightspace
- name: DATABASICS
- name: DNSFilter
- name: DOCOMO Digital
- name: Darwinbox
- name: Dashlane
- name: Databricks
- name: Dataddo
- name: Datadog
- name: Datto Autotask
- name: Deel
- name: Degreed
- name: Deliverect
- name: DemandBase
- name: Demandware
- name: Demodesk
- name: Dependabot
- name: Deputy
- name: DevRev
- name: Dext
- name: Dialpad
- name: Digi
- name: Digio
- name: Discourse
- name: Disqo
- name: Dixa
- name: DocRaptor
- name: Docebo
- name: Docker Hub
- name: Docparser
- name: Docsumo
- name: DocumentPro
- name: Documo
- name: Docusign
- name: Drift
- name: Drip
- name: DriveCentric
- name: DronaHQ
- name: DroneDeploy
- name: Dropbox
- name: Dropbox Sign
- name: Dynatrace
- name: ELMO Software
- name: EPIC
- name: ERPNext
- name: Easyship
- name: EdgeDB
- name: Eightfold
- name: Elastic
- name: Elastic Path
- name: Elementor
- name: ElevenLabs
- name: Elorus
- name: Embrace
- name: Employment Hero
- name: EngageBay
- name: EspoCRM
- name: Etsy
- name: Eventbrite
- name: Everee
- name: Exabeam
- name: Exact Online
- name: Expensify
- name: Expert.ai
- name: F5 Networks
- name: FIS
- name: Facebook Ads
- name: Factorial
- name: Faraday
- name: Fattmerchant
- name: FedEx
- name: Fenergo
- name: Fidel
- name: Figma
- name: Filebase
- name: FinancialForce
- name: Finicity
- name: FireEye
- name: Fireflies
- name: Fiserv
- name: Fivetran
- name: Flexport
- name: Float
- name: Flywire
- name: ForgeRock
- name: Form.io
- name: FormTitan
- name: Formspree
- name: Formstack
- name: Fountain
- name: FreeAgent
- name: Freshbooks
- name: Freshchat
- name: Freshdesk
- name: Freshsales
- name: Freshservice
- name: Front
- name: FullContact
- name: Funraise
- name: G2
- name: Gainsight
- name: Gainsight PX
- name: GameAnalytics
- name: Geoapify
- name: GetAccept
- name: GetResponse
- name: Ghost
- name: Gigasheet
- name: GitBook
- name: GitHub Actions
- name: GitLab
- name: Github
- name: Gladly
- name: Gmail
- name: GoCanvas
- name: GoDial
- name: GoPay
- name: GoTo Webinar
- name: Gong
- name: Google AdSense
- name: Google Address Validation
- name: Google Admin
- name: Google Ads
- name: Google Analytics
- name: Google Big Query
- name: Google Calendar
- name: Google Campaign Manager
- name: Google Classroom
- name: Google Cloud
- name: Google Cloud AI Platform
- name: Google Cloud Dataflow
- name: Google Cloud Translate
- name: Google Cloud Vision
- name: Google Dialogflow
- name: Google Docs
- name: Google Drive
- name: Google Forms
- name: Google Gemini
- name: Google Maps
- name: Google Meet
- name: Google Merchant Center
- name: Google My Business
- name: Google Search Console
- name: Google Security Command Center
- name: Google Sheets
- name: Google Tasks
- name: Google Vertex AI
- name: Gorgias
- name: Grammarly
- name: Greenhouse
- name: GreytHR
- name: Groove
- name: Guru
- name: Gusto
- name: HAProxy
- name: HASH
- name: HERE
- name: HackerOne
- name: Harness
- name: Harvest
- name: Hashi Corp Vault
- name: HashiCorp
- name: Hasura
- name: Heap
- name: HelloSign
- name: HelpNinja
- name: HelpScout
- name: Heroku
- name: HiBob
- name: Highlevel
- name: Hippo Video
- name: Hive
- name: Honeycomb.io
- name: Hootsuite
- name: Hopscotch
- name: Hotjar
- name: Hubspot
- name: Hugging Face Inference API
- name: Humaans
- name: Hunter
- name: IBM API Connect
- name: IBM Cloud
- name: IBM Workspace
- name: IBM X-Force Exchange
- name: IContact
- name: IFTTT
- name: IRIS CRM
- name: Icims
- name: Icinga
- name: ImageKit.io
- name: Imperva
- name: InCountry
- name: InFeedo
- name: Incorta
- name: InfluxDB Cloud
- name: Infor
- name: Ingenico Group
- name: Insider
- name: Insightly
- name: Insightsoftware
- name: Instagram Ads Manager
- name: Instana
- name: Intercom
- name: Intercom Articles
- name: Interswitch Group
- name: Invision Community
- name: Invoice Ninja
- name: Invoiced
- name: Island
- name: Iterable
- name: Iterate.ai
- name: Ivanti
- name: JDBC
- name: JFrog
- name: Jack Henry
- name: JazzHR
- name: Jenkins
- name: Jenkins X
- name: JetBrains YouTrack
- name: Jibble
- name: Jira
- name: Jira Service Desk
- name: JobDiva
- name: Jobadder
- name: Jobnimbus
- name: Jobvite
- name: Jotform
- name: JumpCloud
- name: JupiterOne
- name: Justworks
- name: Karbon
- name: Kashflow
- name: Katalon
- name: Keap
- name: Keatext
- name: Keka
- name: Keycloak
- name: Khoros Marketing
- name: Kickbox
- name: Klaviyo
- name: Klenty
- name: Knack
- name: KnowBe4
- name: Kong
- name: Kount
- name: Labelbox
- name: Lambdatest
- name: Landbot
- name: Laravel Spark
- name: LastPass Enterprise API
- name: LeadGenius
- name: LeadIQ
- name: Leadsquared
- name: Leadzen.ai
- name: Leap
- name: Leapfin
- name: Lemlist
- name: Less Annoying CRM
- name: Lever
- name: Librato
- name: Liferay
- name: Lighthouse
- name: Lightspeed
- name: LimaCharlie
- name: Lime Crm
- name: Linear
- name: LinearB
- name: LinkedIn Ads
- name: Linkedin Campaign Manager
- name: Linkedin Sales Navigator
- name: LiveAgent
- name: LiveChat
- name: Liveperson
- name: Livestorm
- name: Llama AI
- name: LlamaIndex
- name: LogRocket
- name: Logz.io
- name: Looker
- name: Loomio
- name: Loops.so
- name: LoyaltyLion
- name: Lucidworks
- name: Luzmo (Cumul.io)
- name: MParticle
- name: MSG91
- name: Magento
- name: Mailchimp
- name: Mailerlite
- name: Mailgun
- name: Mailmodo
- name: MaintainX
- name: Mambu
- name: Marin Software
- name: Marketo
- name: Mattermark
- name: Mautic
- name: Maximizer
- name: Maxio (Chargify)
- name: Mem
- name: Mendix
- name: Mercury
- name: Message Bird
- name: Metabase
- name: Microsoft Azure SQL Database
- name: Microsoft Defender
- name: Microsoft Dynamics
- name: Microsoft Dynamics 365 Business Central API
- name: Microsoft Dynamics Finance
- name: Microsoft Office 365
- name: Microsoft OneDrive
- name: Microsoft OneNote
- name: Microsoft Power BI
- name: Microsoft Teams
- name: Mindtickle
- name: Miro
- name: Mixpanel
- name: ModMed
- name: Mode
- name: Moengage
- name: Monday
- name: MongoDB
- name: MongoDB Atlas
- name: Moosend
- name: Motion
- name: MyOB
- name: MySQL
- name: N8n.io
- name: NS1
- name: Nano Nets
- name: NationBuilder
- name: NetSuite
- name: Netcore
- name: Netlify
- name: Nets Group
- name: New Relic
- name: Nextcloud
- name: Nicereply
- name: Nimble
- name: NoCRM.io
- name: Nordic API Gateway
- name: Notion
- name: Nylas
- name: OKSign
- name: OPSWAT
- name: OVHcloud
- name: Odoo
- name: Okra
- name: Okta
- name: Omniconvert
- name: Omnisend
- name: OnTask
- name: OneDesk
- name: OneLogin
- name: OnePage CRM
- name: OneTrust
- name: Onna
- name: Ontraport
- name: Open Accounting
- name: OpenAI
- name: OpenBB
- name: OpenText
- name: Opsgenie
- name: OptimoRoute
- name: Oracle Cloud HCM
- name: Oracle DB
- name: Oracle Eloqua
- name: Oracle Field Service
- name: Oracle Financials Cloud
- name: Oracle Fusion - Recruiting Cloud
- name: Oracle Marketing Cloud
- name: Oracle Sales & Fusion Service
- name: Oracle Taleo
- name: Ordoro
- name: Ortto
- name: OutSystems
- name: Outbrain
- name: Outlook
- name: Outplay
- name: Outreach
- name: Oxford Dictionaries
- name: Pabbly
- name: Pachyderm
- name: Paddle
- name: PagerDuty
- name: Palo Alto Prisma Cloud
- name: PandaDoc
- name: Pandle
- name: Panzura
- name: Parallels (Awingu)
- name: Pardot
- name: ParseHub
- name: PartnerStack
- name: PayPal
- name: PayUmoney
- name: Paycor
- name: Paylocity
- name: Paymo
- name: Paystand
- name: Peepl.io
- name: Pendo
- name: PeopleHR
- name: Personio Recruiting
- name: Phantombuster
- name: PhoneBurner
- name: Pickrr
- name: Pinecone
- name: Pingdom
- name: Pipedream
- name: Pipedrive
- name: Pipefy
- name: PipelineCRM
- name: Pipeliner CRM
- name: Pivotal Tracker
- name: Plaid
- name: Plan Grid
- name: Plesk
- name: Plivo
- name: Podio
- name: Podium
- name: PostGrid
- name: PostHog
- name: PostgreSQL
- name: Postman
- name: Postmark
- name: Power Automate
- name: Prisma
- name: Prismic
- name: Process Street
- name: ProcessPlan
- name: Procore
- name: Productboard
- name: Productive.io
- name: Productlane
- name: Proofpoint
- name: Propel
- name: PropelAuth
- name: Propstack
- name: Proxyclick
- name: PubNub
- name: Pulumi
- name: Punchh
- name: Puppet
- name: Pylon
- name: Q2
- name: Qlik
- name: Qualified
- name: Qualys
- name: QuestDB
- name: Quickbase
- name: Quickbooks
- name: Quickbooks Desktop
- name: Quip
- name: Qwilr
- name: Railsbank
- name: Ramp
- name: RapidAPI
- name: Rapyd
- name: Raygun
- name: Razorpay
- name: Recruitee
- name: Recruiterflow
- name: Recurly
- name: Red Hat
- name: Redis
- name: Redox
- name: Repl.it
- name: Reply.io
- name: Rev.ai
- name: Revamp CRM
- name: Revel Systems
- name: RingCentral
- name: Ringover
- name: Rippling
- name: RiskAdvisor
- name: Rocket Chat
- name: RocketReach
- name: Rokt
- name: Rollbar
- name: Routable
- name: Route4Me
- name: Rutter
- name: SAGE Business Cloud
- name: SAP Ariba
- name: SAP C4C
- name: SAP Concur
- name: SAP S/4HANA
- name: SAP Service Cloud
- name: SAP SuccessFactors
- name: SEDNA
- name: SEMrush
- name: SFTP
- name: SMS Magic
- name: SMSBump
- name: SPS Commerce
- name: SQL Server
- name: Sage 300
- name: Sage 50
- name: Sage HR
- name: Sage Intacct
- name: Sage Payroll
- name: Sailthru
- name: SalesBlink
- name: SalesLens
- name: Salesflare
- name: Salesforce
- name: Salesforce CPQ
- name: Salesforce Commerce cloud
- name: Salesforce DMP
- name: Salesforce Financial Services Cloud
- name: Salesforce Marketing Cloud
- name: Salesforce Service Cloud
- name: Saleshood
- name: Salesloft
- name: Salesmate
- name: Samsara
- name: Sapling.ai
- name: SauceLabs
- name: SavvyCal
- name: Scale AI
- name: Scale.com
- name: Scene7
- name: Scout APM
- name: SeaTable
- name: Secure Code Warrior
- name: SecureDocs
- name: SeekWell
- name: Segment
- name: Seismic
- name: Selenium
- name: Semaphore
- name: Semgrep
- name: SendGrid
- name: SendOwl
- name: SendPulse
- name: SendX
- name: Sendbird
- name: Sendcloud
- name: Sendoso
- name: Sensu
- name: SentinelOne
- name: Sentry
- name: SerpApi
- name: ServiceM8
- name: ServiceMax
- name: ServiceNow
- name: Sharepoint
- name: SharpSpring
- name: SheetDB
- name: ShipHero
- name: ShipStation
- name: ShipWorks
- name: Shipamax
- name: Shipbob
- name: Shipcloud
- name: Shipday
- name: ShipperHQ
- name: Shippo
- name: Shopify
- name: Shopline
- name: Shortcut
- name: Showpad
- name: Signal Sciences
- name: SignalFx
- name: Sitecore
- name: Slack
- name: SmartEngage
- name: SmartRecruiters
- name: Smartsheet
- name: Smartsuite
- name: Snapchat Ads
- name: Snowflake
- name: Snowplow Analytics
- name: Snyk
- name: Socket
- name: Socket.IO
- name: Socure
- name: Solar Nexus
- name: SolarWinds Service Desk
- name: Solve CRM
- name: SonarQube
- name: Sonatype
- name: Sophos
- name: Sourceforge
- name: Sourcegraph
- name: Spacelift
- name: Spiff
- name: Splunk
- name: Spotdraft
- name: Spotlightr
- name: Spreedly
- name: Sprinklr
- name: SpruceID
- name: Sqreen
- name: Square
- name: StackBlitz
- name: StackHawk
- name: Stackery
- name: Stackify
- name: Strapi
- name: Stripe
- name: Stripe Atlas
- name: Stripe Corporate Card
- name: Stripe Financial Connections
- name: Stripe Identity
- name: Stripe Tax
- name: Stripe Treasury
- name: StrongDM
- name: Sugar CRM
- name: SugarSync
- name: SumUp
- name: Sumo Logic
- name: Supabase
- name: SuperPhone
- name: SurveyMonkey
- name: SurveySparrow
- name: SwaggerHub
- name: Swell
- name: Switchboard
- name: Symbl.ai
- name: Syniverse
- name: Sysdig
- name: TUNE
- name: Tableau
- name: TalentLMS
- name: TalentReef
- name: Talkdesk
- name: Tally Solutions
- name: Tapform
- name: Tawk.to
- name: Tealium
- name: TeamCity
- name: TeamSupport
- name: TeamWave
- name: Teamleader
- name: Teamtailor
- name: Teamwork Desk
- name: Teamwork.com
- name: Tenable
- name: Terraform
- name: ThoughtSpot
- name: Threat Stack
- name: Ticket Tailor
- name: Tide
- name: Tidio
- name: TikTok Ads
- name: Time Doctor
- name: Tines
- name: Tink
- name: Toast
- name: Todoist
- name: TomTom
- name: Tookan
- name: ToolJet
- name: Totango
- name: Traceable
- name: Tradeshift
- name: Travis CI
- name: Trello
- name: Trengo
- name: Tribe Payments
- name: TrueLayer
- name: Truss
- name: TurboHire
- name: Twilio
- name: Twitter for Business
- name: Tyntec
- name: Typeform
- name: UKG Pro Workforce Management
- name: UKG Ready
- name: UPS
- name: USPS
- name: UiPath
- name: Ukg Pro Recruiting
- name: Unblu
- name: Unbounce
- name: UpBooks
- name: UpKeep
- name: UpLead
- name: Upserve
- name: Upwave
- name: Userflow
- name: Userpilot
- name: VMware
- name: VMware Carbon Black
- name: VTEX
- name: Vanta
- name: Vectara
- name: Veeva
- name: Vend
- name: Vendasta
- name: Veracode
- name: Vercel
- name: Veriff
- name: Very Good Security
- name: VideoAsk
- name: Vimeo
- name: Visor
- name: Vitally
- name: Vtiger
- name: Vultr
- name: WATI
- name: WIX eCommerce
- name: WSO2
- name: Wave Financial
- name: Waylay
- name: WePay
- name: WeSupply
- name: WebMerge
- name: Webengage
- name: Webex
- name: Webflow
- name: Weclapp
- name: Whatfix
- name: Whatsapp
- name: Whereby
- name: Wistia
- name: WooCommerce
- name: Woosender
- name: WorkOS
- name: Workable
- name: Workboard
- name: Workbooks CRM
- name: Workday
- name: Workday Financial Management
- name: Wrike
- name: Wufoo
- name: Xendit
- name: Xero
- name: Yanado
- name: Yapily
- name: Yoast SEO
- name: Yoco
- name: Yodiz
- name: Yotpo
- name: You Can Book Me
- name: YouTube Analytics
- name: Yugabyte
- name: Zabbix
- name: ZenHub
- name: Zendesk
- name: Zendesk Guide
- name: Zendesk Sell
- name: Zendesk Sunshine
- name: Zenefits
- name: Zephyr Scale
- name: ZeroTier
- name: Zeta
- name: Zettle by Paypal
- name: Ziggu
- name: Zing Data
- name: Zoho Analytics
- name: Zoho Assist
- name: Zoho Bigin
- name: Zoho Bookings
- name: Zoho Books
- name: Zoho Bugtracker
- name: Zoho CRM
- name: Zoho Calendar
- name: Zoho Campaigns
- name: Zoho Catalyst
- name: Zoho Cliq
- name: Zoho Commerce
- name: Zoho Creator
- name: Zoho Desk
- name: Zoho Docs
- name: Zoho Expense
- name: Zoho Forms
- name: Zoho Inventory
- name: Zoho Invoice
- name: Zoho Mail
- name: Zoho Meeting
- name: Zoho Notebook
- name: Zoho People
- name: Zoho Projects
- name: Zoho Recruit
- name: Zoho SalesIQ
- name: Zoho Sheet
- name: Zoho Sign
- name: Zoho Sprints
- name: Zoho Subscriptions
- name: Zoho Survey
- name: Zoho WorkDrive
- name: Zoom
- name: Zoom Info
- name: Zulip
- name: Zuora Billing
json_schemas:
- name: Application
  property_count: 6
  slug: application
- name: Config
  property_count: 7
  slug: config
- name: Datastore
  property_count: 4
  slug: datastore
- name: Execution
  property_count: 7
  slug: execution
- name: LinkedAccount
  property_count: 6
  slug: linked-account
- name: Webhook
  property_count: 4
  slug: webhook
- name: Workflow
  property_count: 6
  slug: workflow
jsonld:
- class_count: 0
  name: Cobalt Context
  property_count: 7
  slug: cobalt-context
layout: provider
modified: '2026-05-19'
name: Cobalt
nav: Providers
network: true
overview: 'Cobalt publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Cobalt Hosted API, Config API, and 7 more. Tagged areas include Automation, Embedded iPaaS, and Integrations.


  The Cobalt catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Cobalt''s developer surface includes authentication, getting-started guide, documentation, pricing, signup flow, engineering blog, and 19 more developer resources.'
plans:
- name: Cobalt Plans Pricing
  plan_count: 3
  slug: cobalt-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 5
  name: Cobalt Rate Limits
  slug: cobalt-rate-limits
rules:
- name: Cobalt API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cobalt-jsonschema-spectral-rules
- name: Cobalt API Rules
  rule_count: 13
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 8
  slug: cobalt-rules
score:
  band: strong
  composite: 63.7
  delta: 0.0
  facets:
    commercial_clarity: 92.1
    contract_quality: 69.0
    developer_ergonomics: 43.5
    discoverability: 40.7
    governance: 58.3
    operational_transparency: 63.2
  previous_composite: 63.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cobalt/refs/heads/main/screenshots/cobalt-2026-06-20T174643.png
security:
- kind: authentication
  name: Cobalt Authentication
  slug: cobalt-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Cobalt Domain Security
  slug: cobalt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cobalt Trust Center
  slug: cobalt-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: cobalt
tags:
- Automation
- Embedded iPaaS
- Integrations
use_cases:
- name: Enhancing User Experience and Adoption
- name: Driving SaaS Growth
- name: Revenue Expansion
- name: Competitive Differentiation
- name: Streamlining Business Processes
- name: Automated Workflows
website: https://www.gocobalt.io/
---
