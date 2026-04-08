---
aid: ibm
url: https://raw.githubusercontent.com/api-evangelist/ibm/refs/heads/main/apis.yml
apis:
- name: IBM Watson Assistant
  description: Build conversational interfaces into any application, device, or channel.
  image: https://www.ibm.com/content/dam/connectedassets-adobe-cms/worldwide-content/creative-assets/s-migr/ul/g/8f/c4/watson-assistant.component.complex-narrative-xl-retina.ts=1686660742804.png/content/adobe-cms/us/en/products/watson-assistant/jcr:content/root/table_of_contents/body/content_section_styled/content-section-body/complex_narrative/items/content_group/image
  humanURL: https://www.ibm.com/products/watson-assistant
  baseURL: https://api.us-south.assistant.watson.cloud.ibm.com
  tags:
  - Artificial Intelligence
  - Chatbots
  - Conversational AI
  - NLP
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/assistant/assistant-v2
  - type: openapi
    url: https://raw.githubusercontent.com/watson-developer-cloud/api-spec/master/assistant/assistant-v2.json
  - type: authentication
    url: https://cloud.ibm.com/docs/watson?topic=watson-iam
  - type: getting-started
    url: https://cloud.ibm.com/docs/assistant?topic=assistant-getting-started
- name: IBM Watson Natural Language Understanding
  description: Analyze text to extract metadata from content such as concepts, entities, keywords, categories, sentiment, emotion, relations, and semantic roles.
  humanURL: https://www.ibm.com/cloud/watson-natural-language-understanding
  baseURL: https://api.us-south.natural-language-understanding.watson.cloud.ibm.com
  tags:
  - AI
  - Machine Learning
  - Natural Language Processing
  - Text Analysis
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/natural-language-understanding
  - type: openapi
    url: https://raw.githubusercontent.com/watson-developer-cloud/api-spec/master/natural-language-understanding/natural-language-understanding.json
  - type: pricing
    url: https://www.ibm.com/cloud/watson-natural-language-understanding/pricing
  - type: getting-started
    url: https://cloud.ibm.com/docs/natural-language-understanding
- name: IBM Watson Language Translator
  description: Translate text from one language to another.
  humanURL: https://www.ibm.com/cloud/watson-language-translator
  baseURL: https://api.us-south.language-translator.watson.cloud.ibm.com
  tags:
  - AI
  - Language
  - Translation
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/language-translator
  - type: openapi
    url: https://raw.githubusercontent.com/watson-developer-cloud/api-spec/master/language-translator/language-translator.json
  - type: getting-started
    url: https://cloud.ibm.com/docs/language-translator
- name: IBM Watson Speech to Text
  description: Convert audio voice into written text.
  humanURL: https://www.ibm.com/cloud/watson-speech-to-text
  baseURL: https://api.us-south.speech-to-text.watson.cloud.ibm.com
  tags:
  - AI
  - Audio
  - Speech Recognition
  - Transcription
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/speech-to-text
  - type: openapi
    url: https://raw.githubusercontent.com/watson-developer-cloud/api-spec/master/speech-to-text/speech-to-text.json
  - type: getting-started
    url: https://cloud.ibm.com/docs/speech-to-text
- name: IBM Watson Text to Speech
  description: Convert written text into natural-sounding audio in a variety of languages and voices.
  humanURL: https://www.ibm.com/cloud/watson-text-to-speech
  baseURL: https://api.us-south.text-to-speech.watson.cloud.ibm.com
  tags:
  - AI
  - Audio Generation
  - Text to Speech
  - Voice Synthesis
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/text-to-speech
  - type: openapi
    url: https://raw.githubusercontent.com/watson-developer-cloud/api-spec/master/text-to-speech/text-to-speech.json
  - type: getting-started
    url: https://cloud.ibm.com/docs/text-to-speech
- name: IBM Cloud Object Storage
  description: Store and access unstructured data with built-in high-speed file transfer.
  humanURL: https://www.ibm.com/cloud/object-storage
  baseURL: https://s3.us.cloud-object-storage.appdomain.cloud
  tags:
  - Cloud Storage
  - Object Storage
  - S3 Compatible
  - Storage
  properties:
  - type: documentation
    url: https://cloud.ibm.com/docs/cloud-object-storage/api-reference
  - type: pricing
    url: https://www.ibm.com/cloud/object-storage/pricing
  - type: getting-started
    url: https://cloud.ibm.com/docs/cloud-object-storage
- name: IBM Cloud Databases for PostgreSQL
  description: Managed PostgreSQL database service.
  humanURL: https://www.ibm.com/cloud/databases-for-postgresql
  baseURL: https://api.us-south.databases.cloud.ibm.com
  tags:
  - Cloud
  - Database
  - Managed Database
  - PostgreSQL
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/cloud-databases-api
  - type: getting-started
    url: https://cloud.ibm.com/docs/databases-for-postgresql
- name: IBM Cloud Code Engine
  description: Run containerized workloads without managing servers.
  humanURL: https://www.ibm.com/cloud/code-engine
  baseURL: https://api.us-south.codeengine.cloud.ibm.com
  tags:
  - Cloud Native
  - Containers
  - Platform
  - Serverless
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/codeengine
  - type: cli
    url: https://cloud.ibm.com/docs/codeengine?topic=codeengine-cli
  - type: getting-started
    url: https://cloud.ibm.com/docs/codeengine?topic=codeengine-getting-started
- name: IBM watsonx.ai
  description: Run text inference, prompt tuning, and more on large language models using the watsonx.ai API for generative AI applications.
  humanURL: https://www.ibm.com/products/watsonx-ai
  baseURL: https://us-south.ml.cloud.ibm.com
  tags:
  - Artificial Intelligence
  - Foundation Models
  - Generative AI
  - Large Language Models
  - Machine Learning
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/watsonx-ai
  - type: pricing
    url: https://www.ibm.com/products/watsonx-ai/pricing
  - type: getting-started
    url: https://cloud.ibm.com/docs/watsonxdata
- name: IBM watsonx.governance
  description: Monitor and manage AI models with an enterprise-grade environment that provides visibility into how AI is being built, used, and delivering business value.
  humanURL: https://www.ibm.com/products/watsonx-governance
  baseURL: https://us-south.ml.cloud.ibm.com
  tags:
  - AI Governance
  - Artificial Intelligence
  - Compliance
  - Model Monitoring
  - Trust
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/ai-openscale
  - type: pricing
    url: https://www.ibm.com/products/watsonx-governance/pricing
  - type: getting-started
    url: https://cloud.ibm.com/docs/ai-openscale
- name: IBM Watson Discovery
  description: Add cognitive search and content analytics to applications to identify patterns, trends, and actionable insights from unstructured data.
  humanURL: https://www.ibm.com/products/watson-discovery
  baseURL: https://api.us-south.discovery.watson.cloud.ibm.com
  tags:
  - AI
  - Cognitive Search
  - Content Analytics
  - Document Understanding
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/discovery-data
  - type: getting-started
    url: https://cloud.ibm.com/docs/discovery-data
- name: IBM Cloud Virtual Private Cloud
  description: Provision and manage isolated virtual network environments for compute, storage, and networking resources on IBM Cloud.
  humanURL: https://www.ibm.com/products/vpc
  baseURL: https://us-south.iaas.cloud.ibm.com
  tags:
  - Cloud
  - Compute
  - Infrastructure
  - Networking
  - VPC
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/vpc/latest
  - type: getting-started
    url: https://cloud.ibm.com/docs/vpc
- name: IBM Cloud Kubernetes Service
  description: Create and manage Kubernetes cluster infrastructure to deploy and manage containerized applications on IBM Cloud.
  humanURL: https://www.ibm.com/products/kubernetes-service
  baseURL: https://containers.cloud.ibm.com
  tags:
  - Cloud Native
  - Containers
  - Kubernetes
  - Orchestration
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/kubernetes
  - type: pricing
    url: https://www.ibm.com/cloud/kubernetes-service/pricing
  - type: getting-started
    url: https://cloud.ibm.com/docs/containers?topic=containers-getting-started
- name: IBM Key Protect
  description: Provision and manage encrypted keys for data-at-rest protection across IBM Cloud services.
  humanURL: https://www.ibm.com/products/key-protect
  baseURL: https://us-south.kms.cloud.ibm.com
  tags:
  - Data Protection
  - Encryption
  - Key Management
  - Security
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/key-protect
  - type: getting-started
    url: https://cloud.ibm.com/docs/key-protect
- name: IBM Cloud IAM Identity Services
  description: Manage service IDs, API key identities, trusted profiles, account security settings, and create IAM access tokens.
  humanURL: https://cloud.ibm.com/docs/account?topic=account-iamoverview
  baseURL: https://iam.cloud.ibm.com
  tags:
  - Access Management
  - Authentication
  - Identity
  - Security
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/iam-identity-token-api
  - type: getting-started
    url: https://cloud.ibm.com/docs/account?topic=account-iamoverview
  - type: openapi
    url: openapi/ibm-cloud-iam.yml
  - type: json-schema
    url: json-schema/ibm-cloud-resource-schema.json
  - type: json-ld-context
    url: json-ld/ibm-context.jsonld
- name: IBM Cloud Secrets Manager
  description: Create, lease, and centrally manage secrets used in IBM Cloud services or custom-built applications.
  humanURL: https://www.ibm.com/products/secrets-manager
  baseURL: https://us-south.secrets-manager.appdomain.cloud
  tags:
  - Credentials
  - Secrets
  - Security
  - Vault
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/secrets-manager/secrets-manager-v2
  - type: getting-started
    url: https://cloud.ibm.com/docs/secrets-manager
- name: IBM Cloud Event Notifications
  description: Route event notifications from IBM Cloud services to communication channels such as email, SMS, webhooks, and push notifications.
  humanURL: https://www.ibm.com/products/event-notifications
  baseURL: https://us-south.event-notifications.cloud.ibm.com
  tags:
  - Alerts
  - Events
  - Messaging
  - Notifications
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/event-notifications
  - type: getting-started
    url: https://cloud.ibm.com/docs/event-notifications
- name: IBM Cloud Container Registry
  description: Store and distribute container images in a managed private registry for IBM Cloud Kubernetes and other container workloads.
  humanURL: https://www.ibm.com/products/container-registry
  baseURL: https://us.icr.io
  tags:
  - Container Registry
  - Containers
  - Docker
  - Images
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/container-registry
  - type: getting-started
    url: https://cloud.ibm.com/docs/Registry?topic=Registry-registry_overview
- name: IBM Cloud Schematics
  description: Use Terraform and Ansible to automate the provisioning and configuration management of IBM Cloud resources with infrastructure as code.
  humanURL: https://www.ibm.com/products/schematics
  baseURL: https://us-south.schematics.cloud.ibm.com
  tags:
  - Automation
  - Infrastructure as Code
  - Provisioning
  - Terraform
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/schematics/schematics
  - type: getting-started
    url: https://cloud.ibm.com/docs/schematics?topic=schematics-getting-started
- name: IBM Cloud Internet Services
  description: Provide DDoS protection, global load balancing, DNS management, WAF, and CDN capabilities for internet-facing applications, powered by Cloudflare.
  humanURL: https://www.ibm.com/products/cloud-internet-services
  baseURL: https://api.cis.cloud.ibm.com
  tags:
  - CDN
  - DDoS Protection
  - DNS
  - Security
  - Web Application Firewall
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/cis
  - type: getting-started
    url: https://cloud.ibm.com/docs/cis
- name: IBM Cloudant
  description: Fully managed distributed JSON document database built for the cloud with high availability, durability, and scalability.
  humanURL: https://www.ibm.com/products/cloudant
  baseURL: https://us-south.cloudantnosqldb.appdomain.cloud
  tags:
  - Database
  - Document Database
  - JSON
  - NoSQL
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/cloudant
  - type: getting-started
    url: https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-getting-started-with-cloudant
- name: IBM Event Streams
  description: Fully managed Apache Kafka service for high-throughput event streaming, event ingestion, and event stream distribution between services.
  humanURL: https://www.ibm.com/products/event-automation
  baseURL: https://us-south.event-streams.cloud.ibm.com
  tags:
  - Apache Kafka
  - Event Streaming
  - Messaging
  - Pub/Sub
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/event-streams/adminrest
  - type: getting-started
    url: https://cloud.ibm.com/docs/EventStreams?topic=EventStreams-getting-started
- name: IBM Cloud Security and Compliance Center
  description: Assess, monitor, and remediate security and compliance posture for cloud resources using automated controls and policies.
  humanURL: https://www.ibm.com/products/security-and-compliance-center
  baseURL: https://us-south.compliance.cloud.ibm.com
  tags:
  - Compliance
  - Governance
  - Risk Management
  - Security
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/security-compliance
  - type: getting-started
    url: https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-getting-started
- name: IBM Cloud Functions
  description: Run lightweight code that executes application logic in a scalable way using an event-driven serverless compute platform based on Apache OpenWhisk.
  humanURL: https://cloud.ibm.com/functions
  baseURL: https://us-south.functions.cloud.ibm.com
  tags:
  - Apache OpenWhisk
  - Event-Driven
  - Functions as a Service
  - Serverless
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/functions
  - type: getting-started
    url: https://cloud.ibm.com/docs/openwhisk
- name: IBM Cloud DNS Services
  description: Manage private DNS zones and resolution for IBM Cloud VPC networks.
  humanURL: https://www.ibm.com/products/dns
  baseURL: https://api.dns-svcs.cloud.ibm.com
  tags:
  - DNS
  - Domain Management
  - Networking
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/dns-svcs
  - type: getting-started
    url: https://cloud.ibm.com/docs/dns-svcs?topic=dns-svcs-getting-started
- name: IBM Cloud Monitoring
  description: Gain operational visibility into the performance and health of applications, services, and platforms running on IBM Cloud.
  humanURL: https://www.ibm.com/products/cloud-monitoring
  baseURL: https://us-south.monitoring.cloud.ibm.com
  tags:
  - Alerting
  - Metrics
  - Monitoring
  - Observability
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/monitor
  - type: getting-started
    url: https://cloud.ibm.com/docs/monitoring
- name: IBM Cloud Logs
  description: A scalable logging service for persisting, querying, tailing, and visualizing logs across IBM Cloud resources.
  humanURL: https://cloud.ibm.com/catalog/services/cloud-logs
  baseURL: https://us-south.logs.cloud.ibm.com
  tags:
  - Log Analysis
  - Logging
  - Observability
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/logs-service-api
  - type: getting-started
    url: https://cloud.ibm.com/docs/cloud-logs
- name: IBM Cloud Activity Tracker
  description: Configure and manage auditing events to track how users and applications interact with IBM Cloud services and resources.
  humanURL: https://cloud.ibm.com/catalog/services/activity-tracker
  baseURL: https://us-south.atracker.cloud.ibm.com
  tags:
  - Activity Tracking
  - Auditing
  - Compliance
  - Observability
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/atracker
  - type: getting-started
    url: https://cloud.ibm.com/docs/activity-tracker
- name: IBM Cloud App ID
  description: Add authentication and authorization to web and mobile applications with identity management, social login, and multi-factor authentication.
  humanURL: https://www.ibm.com/products/app-id
  baseURL: https://us-south.appid.cloud.ibm.com
  tags:
  - Authentication
  - Authorization
  - Identity
  - Security
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/app-id/management
  - type: getting-started
    url: https://cloud.ibm.com/docs/appid
- name: IBM Cloud Transit Gateway
  description: Interconnect IBM Cloud VPCs, classic infrastructure, and on-premises networks through a single gateway for simplified network management.
  humanURL: https://www.ibm.com/products/transit-gateway
  baseURL: https://transit.cloud.ibm.com
  tags:
  - Connectivity
  - Hybrid Cloud
  - Networking
  - Transit Gateway
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/transit-gateway
  - type: getting-started
    url: https://cloud.ibm.com/docs/transit-gateway
- name: IBM Cloud Resource Controller
  description: Manage the lifecycle of IBM Cloud resources in a customer account including provisioning, binding, and managing access to resource instances.
  humanURL: https://cloud.ibm.com/docs/account?topic=account-manage_resource
  baseURL: https://resource-controller.cloud.ibm.com
  tags:
  - Cloud Management
  - Provisioning
  - Resource Management
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/resource-controller/resource-controller
- name: IBM Cloud Global Search
  description: Search for cloud resources across the IBM Cloud platform using resource attributes and properties.
  humanURL: https://cloud.ibm.com/docs/account?topic=account-tag
  baseURL: https://api.global-search-tagging.cloud.ibm.com
  tags:
  - Cloud Management
  - Resource Discovery
  - Search
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/search
- name: IBM Cloud Global Tagging
  description: Create, delete, search, attach, or detach tags to organize and manage IBM Cloud resources.
  humanURL: https://cloud.ibm.com/docs/account?topic=account-tag
  baseURL: https://tags.global-search-tagging.cloud.ibm.com
  tags:
  - Organization
  - Resource Management
  - Tagging
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/tagging
- name: IBM IAM Policy Management
  description: Create and manage access policies that control what actions users can perform on IBM Cloud resources.
  humanURL: https://cloud.ibm.com/docs/account?topic=account-userroles
  baseURL: https://iam.cloud.ibm.com
  tags:
  - Access Control
  - IAM
  - Policies
  - Security
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/iam-policy-management
  - type: openapi
    url: openapi/ibm-cloud-iam.yml
  - type: json-schema
    url: json-schema/ibm-cloud-resource-schema.json
  - type: json-ld-context
    url: json-ld/ibm-context.jsonld
- name: IBM IAM Access Groups
  description: Create and manage access groups to organize users and service IDs into groups for simplified access management.
  humanURL: https://cloud.ibm.com/docs/account?topic=account-groups
  baseURL: https://iam.cloud.ibm.com
  tags:
  - Access Groups
  - Access Management
  - IAM
  - Security
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/iam-access-groups
  - type: openapi
    url: openapi/ibm-cloud-iam.yml
  - type: json-schema
    url: json-schema/ibm-cloud-resource-schema.json
  - type: json-ld-context
    url: json-ld/ibm-context.jsonld
- name: IBM Cloud Power Virtual Server
  description: Deploy and manage AIX, IBM i, and Linux workloads on IBM Power Systems virtual servers in the IBM Cloud.
  humanURL: https://www.ibm.com/products/power-virtual-server
  baseURL: https://us-south.power-iaas.cloud.ibm.com
  tags:
  - AIX
  - IBM I
  - Infrastructure
  - Power Systems
  - Virtual Server
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/power-cloud
  - type: getting-started
    url: https://cloud.ibm.com/docs/power-iaas
- name: IBM Cloud Enterprise Management
  description: Create and manage enterprise accounts, account groups, and child accounts for centralized billing and usage tracking.
  humanURL: https://cloud.ibm.com/docs/account?topic=account-enterprise
  baseURL: https://enterprise.cloud.ibm.com
  tags:
  - Account Management
  - Billing
  - Enterprise
  - Multi-Account
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/enterprise-apis/enterprise
- name: IBM Cloud Projects
  description: Configure, deploy, and govern infrastructure as code resources at scale using projects for managed deployments.
  humanURL: https://cloud.ibm.com/docs/secure-enterprise?topic=secure-enterprise-understanding-projects
  baseURL: https://projects.api.cloud.ibm.com
  tags:
  - Configuration
  - Deployment
  - Governance
  - Infrastructure as Code
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/projects
  - type: getting-started
    url: https://cloud.ibm.com/docs/secure-enterprise?topic=secure-enterprise-understanding-projects
- name: IBM watsonx.data
  description: Collect, store, query, and analyze structured and unstructured enterprise data with a unified data lakehouse platform optimized for price and performance.
  humanURL: https://www.ibm.com/products/watsonx-data
  baseURL: https://us-south.lakehouse.cloud.ibm.com
  tags:
  - AI Data
  - Analytics
  - Data Lakehouse
  - Data Management
  - Open Source
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/watsonxdata-software
  - type: pricing
    url: https://www.ibm.com/products/watsonx-data/pricing
  - type: getting-started
    url: https://dataplatform.cloud.ibm.com/docs/?context=wx
- name: IBM API Connect
  description: Create, secure, manage, share, monetize, and analyze APIs across clouds with a comprehensive end-to-end API management solution.
  humanURL: https://www.ibm.com/products/api-connect
  baseURL: https://api.us-south.apiconnect.cloud.ibm.com
  tags:
  - API Gateway
  - API Management
  - API Security
  - Developer Portal
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/apiconnect/apic-management-api
  - type: getting-started
    url: https://cloud.ibm.com/docs/apiconnect?topic=apiconnect-getting-started
- name: IBM Cloud Direct Link
  description: Establish private, high-speed connectivity between on-premises networks and IBM Cloud without traversing the public internet.
  humanURL: https://www.ibm.com/products/direct-link
  baseURL: https://directlink.cloud.ibm.com
  tags:
  - Connectivity
  - Hybrid Cloud
  - Networking
  - Private Network
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/direct_link
  - type: getting-started
    url: https://cloud.ibm.com/docs/dl?topic=dl-get-started-with-ibm-cloud-dl
- name: IBM Cloud Continuous Delivery Toolchain
  description: Create and manage toolchains that integrate development, deployment, and operations tools for continuous delivery workflows.
  humanURL: https://www.ibm.com/products/continuous-delivery
  baseURL: https://api.us-south.devops.cloud.ibm.com
  tags:
  - CI/CD
  - Continuous Delivery
  - DevOps
  - Toolchain
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/toolchain
  - type: getting-started
    url: https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-getting-started
- name: IBM Cloud Tekton Pipeline
  description: Create and manage Tekton-based continuous integration and continuous delivery pipelines within Kubernetes clusters.
  humanURL: https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-tekton-pipelines
  baseURL: https://api.us-south.devops.cloud.ibm.com
  tags:
  - CI/CD
  - DevOps
  - Kubernetes
  - Pipelines
  - Tekton
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/tekton-pipeline
  - type: getting-started
    url: https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-tekton-pipelines
- name: IBM Cloud User Management
  description: Manage users within an IBM Cloud account including inviting, retrieving, updating, or removing users and managing user profiles and settings.
  humanURL: https://cloud.ibm.com/docs/account?topic=account-iamuserinv
  baseURL: https://user-management.cloud.ibm.com
  tags:
  - Account Management
  - IAM
  - Identity
  - User Management
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/user-management
- name: IBM Cloud Usage Reports
  description: Retrieve usage details and costs for IBM Cloud resources in an account reported by the month in which they were incurred.
  humanURL: https://cloud.ibm.com/docs/billing-usage?topic=billing-usage-viewingusage
  baseURL: https://billing.cloud.ibm.com
  tags:
  - Billing
  - Cost Management
  - Reporting
  - Usage
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/metering-reporting
- name: IBM Cloud Global Catalog
  description: Manage the system of record for IBM Cloud products across geographies including compute, storage, networking, and cloud-native services.
  humanURL: https://cloud.ibm.com/catalog
  baseURL: https://globalcatalog.cloud.ibm.com
  tags:
  - Catalog
  - Product Catalog
  - Resource Management
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/resource-catalog/global-catalog
- name: IBM Cloud Catalog Management
  description: Define how users in an account interact with the IBM Cloud catalog and manage private catalogs for curated product offerings.
  humanURL: https://cloud.ibm.com/docs/account?topic=account-filter-account
  baseURL: https://cm.globalcatalog.cloud.ibm.com
  tags:
  - Catalog Management
  - Governance
  - Private Catalog
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/resource-catalog/private-catalog
- name: IBM Cloud Context-based Restrictions
  description: Create and manage network zones and context-based restriction rules to control access to IBM Cloud resources based on network context.
  humanURL: https://cloud.ibm.com/docs/account?topic=account-context-restrictions-whatis
  baseURL: https://cbr.cloud.ibm.com
  tags:
  - Access Control
  - Network Security
  - Restrictions
  - Security
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/context-based-restrictions
  - type: getting-started
    url: https://cloud.ibm.com/docs/account?topic=account-context-restrictions-create
- name: IBM Cloud Databases for Redis
  description: Fully managed Redis in-memory data store for caching, session management, and high-speed data access on IBM Cloud.
  humanURL: https://www.ibm.com/products/databases-for-redis
  baseURL: https://api.us-south.databases.cloud.ibm.com
  tags:
  - Caching
  - Database
  - In-Memory
  - Managed Database
  - Redis
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5
  - type: getting-started
    url: https://cloud.ibm.com/docs/databases-for-redis
- name: IBM Cloud Databases for MongoDB
  description: Fully managed MongoDB document database service with built-in high availability, automated backups, and scaling on IBM Cloud.
  humanURL: https://www.ibm.com/products/databases-for-mongodb
  baseURL: https://api.us-south.databases.cloud.ibm.com
  tags:
  - Database
  - Document Database
  - Managed Database
  - MongoDB
  - NoSQL
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5
  - type: getting-started
    url: https://cloud.ibm.com/docs/databases-for-mongodb?topic=databases-for-mongodb-getting-started-new
- name: IBM Cloud Databases for Elasticsearch
  description: Fully managed Elasticsearch service for full-text search, log analytics, and application monitoring on IBM Cloud.
  humanURL: https://www.ibm.com/products/databases-for-elasticsearch
  baseURL: https://api.us-south.databases.cloud.ibm.com
  tags:
  - Database
  - Elasticsearch
  - Log Analytics
  - Managed Database
  - Search
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5
  - type: getting-started
    url: https://cloud.ibm.com/docs/databases-for-elasticsearch
- name: IBM Cloud Enterprise Billing Units
  description: Manage billing units, billing options, and credit pools for IBM Cloud enterprise accounts.
  humanURL: https://cloud.ibm.com/docs/billing-usage?topic=billing-usage-viewingusage
  baseURL: https://billing.cloud.ibm.com
  tags:
  - Billing
  - Cost Management
  - Credit Management
  - Enterprise
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/enterprise-apis/billing-unit
- name: IBM Cloud Enterprise Usage Reports
  description: Access usage reports for entities managed by an IBM Cloud enterprise including enterprises, account groups, and accounts.
  humanURL: https://cloud.ibm.com/docs/billing-usage?topic=billing-usage-viewingusage
  baseURL: https://enterprise.cloud.ibm.com
  tags:
  - Analytics
  - Cost Management
  - Enterprise
  - Usage Reports
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/enterprise-apis/resource-usage-reports
- name: IBM Cloud VMware Solutions
  description: Deploy and manage VMware workloads on IBM Cloud infrastructure with automated provisioning and lifecycle management.
  humanURL: https://www.ibm.com/products/vmware
  baseURL: https://api.us-south.vmware.cloud.ibm.com
  tags:
  - Hybrid Cloud
  - Infrastructure
  - Virtualization
  - VMware
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/vmware-solutions
  - type: getting-started
    url: https://cloud.ibm.com/docs/vmwaresolutions
- name: IBM watsonx.ai Runtime
  description: Build, train, and deploy machine learning models with a full range of tools and services for data science and AI lifecycle management.
  humanURL: https://www.ibm.com/products/watsonx-ai
  baseURL: https://us-south.ml.cloud.ibm.com
  tags:
  - AI
  - Data Science
  - Machine Learning
  - Model Deployment
  - Model Training
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/machine-learning
  - type: getting-started
    url: https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-api.html?context=wx
- name: IBM Knowledge Catalog
  description: Discover, catalog, categorize, and govern data assets and AI models with an intelligent data catalog for enterprise data governance.
  humanURL: https://www.ibm.com/products/knowledge-catalog
  baseURL: https://api.dataplatform.cloud.ibm.com
  tags:
  - AI Governance
  - Data Catalog
  - Data Governance
  - Metadata Management
  properties:
  - type: documentation
    url: https://cloud.ibm.com/apidocs/knowledge-catalog
name: IBM
tags:
- API Management
- Artificial Intelligence
- Billing
- Cloud Computing
- Containers
- Data Governance
- Databases
- DevOps
- Enterprise
- Generative AI
- Hybrid Cloud
- Infrastructure
- Machine Learning
- Networking
- Observability
- Security
- Serverless
- Storage
- Watson
- Watsonx
type: Contract
image: https://www.ibm.com/brand/experience-guides/developer/b1db1ae501d522a1a4b49613fe07c9f1/01_8-bar-positive.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: A collection of IBM's public APIs and developer resources.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

