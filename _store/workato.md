---
aid: workato
url: https://raw.githubusercontent.com/api-evangelist/workato/refs/heads/main/apis.yml
apis:
  - aid: workato:workato
    name: Workato
    tags:
      - Agentic
      - Embedded SaaS Integration
      - iPaaS
      - Orchestration
    humanURL: https://www.workato.com/
    properties:
      - url: https://www.workato.com/
        type: Documentation
      - url: https://docs.workato.com/en/workato-api.html#base-url
        name: Workato API - Introduction | Workato Docs
        type: Documentation
        description: 'null'
      - url: https://docs.workato.com/en/workato-api.html#authentication
        name: Workato API - Introduction | Workato Docs
        type: Authentication
        description: 'null'
      - url: https://docs.workato.com/workato-api.html
        name: Workato Developer API - Introduction
        type: API Documentation
      - url: https://docs.workato.com/workato-api/resources.html
        name: Workato API - Resources
        type: API Reference
      - url: https://docs.workato.com/workato-api/recipes.html
        name: Workato API - Recipes
        type: API Reference
      - url: https://docs.workato.com/workato-api/api-connectors.html
        name: Workato API - Connectors
        type: API Reference
      - url: https://docs.workato.com/workato-api/api-client-apis.html
        name: Workato API - API Clients
        type: API Reference
      - url: https://docs.workato.com/workato-api/api-platform.html
        name: Workato API - API Platform
        type: API Reference
      - url: https://docs.workato.com/workato-api/custom_connectors.html
        name: Workato API - Custom Connectors
        type: API Reference
      - url: https://docs.workato.com/workato-api/recipe-lifecycle-management.html
        name: Workato API - Recipe Lifecycle Management
        type: API Reference
      - url: https://docs.workato.com/workato-api/authentication.html
        name: Workato API - Authentication
        type: Authentication
      - url: https://docs.workato.com/workato-api/rate-limiting.html
        name: Workato API - Rate Limiting
        type: Rate Limits
      - url: https://docs.workato.com/developing-connectors/sdk.html
        name: Workato Connector SDK - Developer Program
        type: SDK
      - url: https://github.com/workato/workato-connector-sdk
        name: Workato Connector SDK - GitHub
        type: SDK
      - url: https://docs.workato.com/developing-connectors/custom-connector.html
        name: Create a Custom Connector
        type: SDK
      - url: https://docs.workato.com/workato-api/pubsub.html
        name: Workato API - Event Streams Public API
        type: API Reference
      - url: https://docs.workato.com/workato-api/agent-studio.html
        name: Workato API - Agent Studio
        type: API Reference
      - url: https://docs.workato.com/workato-api/mcp-servers.html
        name: Workato API - MCP Servers
        type: API Reference
      - url: https://docs.workato.com/workato-api/test-automation.html
        name: Workato API - Test Automation
        type: API Reference
      - url: https://docs.workato.com/workato-api/data-tables.html
        name: Workato API - Data Tables
        type: API Reference
      - url: https://docs.workato.com/workato-api/tag-assignments.html
        name: Workato API - Tag Assignments
        type: API Reference
      - url: https://docs.workato.com/workato-api/custom-oauth-profiles.html
        name: Workato API - Custom OAuth Profiles
        type: API Reference
      - url: openapi/workato-developer-api-openapi.yml
        type: OpenAPI
      - url: openapi/workato-agent-studio-openapi.yml
        type: OpenAPI
      - url: json-schema/workato-recipe-schema.json
        type: JSONSchema
      - url: json-schema/workato-genie-schema.json
        type: JSONSchema
    description: Workato is an American multinational software company that provides a cloud-based platform for automation, integration, and artificial intelligence orchestration across applications, data, and systems. The company was founded in 2013 and is headquartered in Mountain View, California.
  - aid: workato:embedded-api
    name: Workato Embedded Partner API
    tags:
      - Embedded iPaaS
      - OEM
      - Partner API
    humanURL: https://docs.workato.com/oem/oem-api.html
    properties:
      - url: https://docs.workato.com/oem/oem-api.html
        name: Embedded Partner APIs
        type: API Documentation
      - url: https://docs.workato.com/oem/oem-api/managed-users.html
        name: Embedded API - Managed Customers
        type: API Reference
      - url: https://docs.workato.com/oem/oem-api/connections.html
        name: Embedded API - Connections
        type: API Reference
      - url: https://docs.workato.com/oem/oem-api/api-platform.html
        name: Embedded API - API Platform
        type: API Reference
      - url: https://docs.workato.com/oem/oem-api/adapters.html
        name: Embedded API - Connectors
        type: API Reference
      - url: https://docs.workato.com/oem/oem-api/jobs
        name: Embedded API - Jobs
        type: API Reference
      - url: https://docs.workato.com/oem/oem-api/team.html
        name: Embedded API - Customer Workspace Collaborators
        type: API Reference
      - url: https://docs.workato.com/oem/embedded-environments/embedded-environments-api.html
        name: Embedded Environments APIs
        type: API Reference
      - url: https://docs.workato.com/oem/oem-api-faqs.html
        name: Embedded Partner API FAQs
        type: FAQ
      - url: https://docs.workato.com/oem.html
        name: Workato Embedded Documentation
        type: Documentation
      - url: https://docs.workato.com/oem/workato-embedded.html
        name: Workato Fully Embedded
        type: Documentation
    description: The Workato Embedded Partner APIs enable partners to programmatically create and manage customers, recipes, connections, and other assets within the Workato Embedded platform. These APIs support provisioning customer workspaces, managing environments, and building fully embedded integration experiences within partner applications.
  - aid: workato:event-streams-public-api
    name: Workato Event Streams Public API
    tags:
      - Event Streams
      - Messaging
      - Pub/Sub
      - REST
    humanURL: https://docs.workato.com/workato-api/pubsub.html
    properties:
      - url: https://docs.workato.com/workato-api/pubsub.html
        name: Workato API - Event Streams Public API
        type: Documentation
      - url: https://docs.workato.com/event-streams.html
        name: Event Streams | Workato Docs
        type: Documentation
      - url: openapi/workato-event-streams-openapi.yml
        type: OpenAPI
      - url: asyncapi/workato-event-streams-asyncapi.yml
        type: AsyncAPI
    description: The Workato Event Streams Public API enables HTTP-based clients to publish and consume messages from event topics. It supports single message publish, batch publish of up to 100 messages, and message consumption with long polling. The API is separate from the Developer API's event streams management endpoints and is rate limited to 60 requests per minute with a 1 MB maximum payload.
  - aid: workato:mcp-server-api
    name: Workato MCP Server API
    tags:
      - AI Agents
      - MCP
      - Model Context Protocol
      - REST
    humanURL: https://docs.workato.com/mcp.html
    properties:
      - url: https://docs.workato.com/mcp.html
        name: MCP | Workato Docs
        type: Documentation
      - url: https://docs.workato.com/workato-api/mcp-servers.html
        name: Workato API - MCP Servers
        type: API Reference
      - url: https://docs.workato.com/en/mcp/expose-developer-apis.html
        name: Workato Developer API MCP | Workato Docs
        type: Documentation
      - url: openapi/workato-mcp-server-openapi.yml
        type: OpenAPI
    description: The Workato MCP Server API provides endpoints for creating, configuring, and managing Model Context Protocol (MCP) servers that expose Workato API collections as tools for AI agents. It supports server creation, tool management, user group assignment, and policy configuration. MCP servers generate unique authenticated URLs usable by AI development environments like Claude Desktop and Cursor.
name: Workato
tags:
  - Agentic
  - API Management
  - Automation
  - B2B
  - Embedded iPaaS
  - Enterprise
  - Integration
  - iPaaS
  - Orchestration
  - Workflow
type: Index
image: https://www.workato.com/wp-content/uploads/2023/01/workato-logo.svg
access: 3rd-Party
common:
  - url: https://github.com/workato
    name: GitHub Organization
    type: GitHubOrganization
  - url: https://www.workato.com/pricing
    name: "Workato Pricing Model: Here\x19s How It Works | Workato"
    type: Pricing
    description: 'null'
  - url: https://www.workato.com/platform/security
    name: Automation Governance and Data Security | Workato
    type: Security
    description: 'null'
  - url: https://www.workato.com/use_cases
    data:
      - name: Actions by LLM Accelerator
        description: Pre-built solution to automate enterprise action with LLM & Workato
      - name: SAP Order-to-Cash Accelerator
        description: Accelerate order to cash process implementation using SAP S/4 HANA with Salesforce CRM
      - name: Salesforce Workbot Accelerator
        description: Access Salesforce Seamlessly in Slack
      - name: Atlassian Virtual Agent Accelerator
        description: Real-time request fulfilment and response to the users from Atlassian Virtual Agent
      - name: NetSuite to Salesforce integration Accelerator
        description: Automate lead-to-cash processes and get real-time visibility into back-office order, fulfillment, and financial operations
      - name: Workday Revenue Management
        description: Helps organizations in syncing their CPQ orders from CRM into WRM as a contract
      - name: Security Orchestration, Automation & Response (SOAR) (AI@Work)
        description: Elevate your Security Posture with AI-Driven SOAR Excellence
      - name: Intelligent Invoice Processing
        description: Experience AI-powered efficiency and superior accuracy in invoice processing with Cloudorizon's solution
      - name: Automation Training Manager
        description: Provide personalized training plans based on individual learning needs
      - name: Sales Process & Forecasting Alignment
        description: The first step in achieving Pipeline Resilience
      - name: MindAssist
        description: MindAssist automates support ticket creation & bot retriggering for Automation Anywhere A360, helping businesses build resilient automations with Workato's low-code platform.
      - name: Software License Optimization
        description: Automate the process of identifying & deprovisioning underutilized app licenses
      - name: AIML Accelerator
        description: Power up your automations using AIML PLatforms within your recipe
      - name: Automation Quality & Security
        description: Standardize and automate quality and security best practices for your automations
      - name: IT Help Desk Bot
        description: Supercharge your helpdesk with self-service knowledge articles & service requests powered by intelligent bots
      - name: OPA Manager
        description: A standardized approach to automate the add agents, manage and troubleshoot OPAs
      - name: App Provision/Deprovisioning
        description: Manage user access to applications Leverage a standardized approach to manage user access to applications
      - name: Product-Led Sales
        description: Take action on account signals at scale to increase customer acquisition, retention & expansion
      - name: Order-to-Cash
        description: Transform your order-to-cash process into a competitive differentiator
      - name: Employee Onboarding
        description: Improve the scale, speed & experience of your employee onboarding with fewer resources
      - name: Productized Integrations
        description: Supercharge your product with pre-built integrations to apps your customers need
      - name: Centralize Integration/Automation
        description: Harness the power of integration + automation across teams without sacrificing agility
      - name: Enterprise Data Hub
        description: Create a standardized and trusted source of truth for your critical records
      - name: Campaign Launchpad
        description: Standardize your marketing campaign process & launch faster with automation
      - name: Autonomous Operations Framework
        description: Error handling, logging, notification, and automated recovery framework
      - name: Approvals bot for Slack/Teams
        description: Faster and easier approvals by utilizing Slack and Teams
      - name: ELT Pipeline for Snowflake
        description: Standardized framework for ingesting data into Snowflake for reporting and analytics
      - name: Back-to-Office Process
        description: Help your employees return to the office with a templatized framework
      - name: CI/CD Automation
        description: Leverage a standardized approach to manage recipe promotion between Workato environments
    name: Popular Use Cases
    type: UseCases
    description: 'null'
  - url: https://www.workato.com/solutions/
    name: Workato Solutions
    type: Solutions
  - url: https://www.workato.com/solutions/
    data:
      - name: Order-to-Cash
        url: https://www.workato.com/use_cases/order_to_cash
        features:
          - Order To Cash
          - ERP Integration
          - CRM Automation
          - Invoice Processing
          - Revenue Operations
          - Deal Desk Automation
          - Days Sales Outstanding
      - name: Employee Onboarding
        url: https://www.workato.com/use_cases/employee_onboarding
        features:
          - Employee Onboarding
          - HR Automation
          - ATS Integration
          - HRIS Integration
          - Application Provisioning
          - Talent Acquisition
          - Workflow Automation
      - name: Product-Led Sales
        url: https://www.workato.com/use_cases/product_led_sales
        features:
          - Product Led Sales
          - Customer 360
          - Reverse ETL
          - Go-To-Market Automation
          - Sales Signals
          - Data Synchronization
          - Revenue Operations
      - name: IT Automation
        url: https://www.workato.com/editions/it
        features:
          - IT Automation
          - Incident Management
          - Help Desk
          - Employee Onboarding
          - ChatOps
          - Access Management
          - Workflow Automation
      - name: Finance Automation
        url: https://www.workato.com/editions/finance
        features:
          - Finance Automation
          - Order To Cash
          - Accounts Payable
          - Financial Reporting
          - Month End Close
          - ERP Integration
          - Revenue Realization
      - name: HR Automation
        url: https://www.workato.com/editions/hr
        features:
          - HR Automation
          - Talent Acquisition
          - Employee Onboarding
          - People Operations
          - Offboarding
          - Workday Integration
          - Workflow Automation
      - name: Sales Automation
        url: https://www.workato.com/editions/sales
        features:
          - Sales Automation
          - Lead To Opportunity
          - Deal Desk
          - Order To Cash
          - Account Management
          - CRM Integration
          - Pipeline Management
      - name: Marketing Operations
        url: https://www.workato.com/editions/marketing
        features:
          - Marketing Automation
          - Campaign Operations
          - Lead Management
          - Data Orchestration
          - CRM Integration
          - Demand Generation
          - Customer Journey
      - name: Support Automation
        url: https://www.workato.com/editions/support
        features:
          - Support Automation
          - Customer Experience
          - Ticket Management
          - Churn Prevention
          - Customer Intelligence
          - Mean Time To Resolution
          - AI Powered Support
      - name: Revenue Operations
        url: https://www.workato.com/revops
        features:
          - Revenue Operations
          - Pipeline Generation
          - Deal Management
          - Customer Retention
          - Sales Operations
          - Marketing Operations
          - Customer Success
      - name: Manufacturing
        url: https://www.workato.com/industry/manufacturing
        features:
          - Manufacturing Automation
          - Supply Chain
          - Factory Automation
          - ERP Integration
          - Inventory Management
          - Workforce Productivity
          - Data Integration
      - name: Financial Services
        url: https://www.workato.com/industry/financial_services
        features:
          - Financial Services
          - Banking Automation
          - KYC AML Compliance
          - Customer Onboarding
          - Claims Processing
          - Regulatory Reporting
          - AI Agents
      - name: Retail
        url: https://www.workato.com/industry/retail
        features:
          - Retail Automation
          - Order Management
          - Inventory Synchronization
          - Supply Chain
          - EDI Integration
          - E-Commerce Integration
          - Omnichannel
      - name: Logistics
        url: https://www.workato.com/industry/logistics
        features:
          - Logistics Automation
          - Supply Chain Visibility
          - Quote To Cash
          - Workforce Optimization
          - Green Logistics
          - Partner Portal Integration
          - Administrative Automation
      - name: Healthcare
        url: https://www.workato.com/industry/healthcare
        features:
          - Healthcare Automation
          - Patient Data Integration
          - Compliance Automation
          - Interoperability
          - Value Based Care
          - Legacy System Integration
          - Regulatory Compliance
      - name: Media
        url: https://www.workato.com/industry/media
        features:
          - Media Automation
          - Content Distribution
          - Hyper Personalization
          - Campaign Optimization
          - Media Production
          - Data Integration
          - Workflow Automation
    name: Use Cases
    type: UseCases
  - url: https://www.workato.com/resources
    name: Resources Library | Workato
    type: Resources
    description: 'null'
  - url: https://www.workato.com/the-connector/
    name: Workato Blog | Content for IT and RevOps professionals
    type: Blog
    description: 'null'
  - url: https://www.workato.com/product-hub/whats-new/
    name: Whats New | Product Hub
    type: ' WhatsNew'
    description: 'null'
  - url: https://www.workato.com/product-hub/whats-new/
    name: Whats New | Product Hub
    type: ' WhatsNew'
    description: 'null'
  - url: https://www.workato.com/product-hub/changelog/
    name: Changelog Archive | Workato Product Hub
    type: ChangeLog
    description: 'null'
  - url: https://www.workato.com/the-connector/category/customer-stories/americas/
    name: Americas Archives
    type: Customers
    description: 'null'
  - url: https://partners.workato.com/consultants
    name: Find the right Workato Service Partner
    type: Partners
    description: 'null'
  - url: https://docs.workato.com/en/
    name: Workato Docs
    type: Portal
    description: 'null'
  - url: https://docs.workato.com/en/
    name: Workato Docs
    type: Portal
    description: 'null'
  - url: https://app.workato.com/browse/recipes
    data:
      - aid: 0codekit
        url: https://app.workato.com/browse/recipes?q=app:0codekit
        name: 0codekit
      - aid: 10,000ft
        url: https://app.workato.com/browse/recipes?q=app:10,000ft
        name: 10,000ft
      - aid: 3-d-repo
        url: https://app.workato.com/browse/recipes?q=app:3-d-repo
        name: 3 D Repo
      - aid: abbyy-flexicapture
        url: https://app.workato.com/browse/recipes?q=app:abbyy-flexicapture
        name: Abbyy Flexicapture
      - aid: abbyy-vantage
        url: https://app.workato.com/browse/recipes?q=app:abbyy-vantage
        name: Abbyy Vantage
      - aid: abuseipdb
        url: https://app.workato.com/browse/recipes?q=app:abuseipdb
        name: AbuseIPDB
      - aid: accredible
        url: https://app.workato.com/browse/recipes?q=app:accredible
        name: Accredible
      - aid: action-network
        url: https://app.workato.com/browse/recipes?q=app:action-network
        name: Action Network
      - aid: acumatica-erp
        url: https://app.workato.com/browse/recipes?q=app:acumatica-erp
        name: Acumatica ERP
      - aid: adaptive-insights
        url: https://app.workato.com/browse/recipes?q=app:adaptive-insights
        name: Adaptive Insights
      - aid: adaptive-shield
        url: https://app.workato.com/browse/recipes?q=app:adaptive-shield
        name: Adaptive Shield
      - aid: address-validator
        url: https://app.workato.com/browse/recipes?q=app:address-validator
        name: Address Validator
      - aid: adeona-pim
        url: https://app.workato.com/browse/recipes?q=app:adeona-pim
        name: Adeona PIM
      - aid: adobe-admin
        url: https://app.workato.com/browse/recipes?q=app:adobe-admin
        name: Adobe Admin
      - aid: adobe-sign
        url: https://app.workato.com/browse/recipes?q=app:adobe-sign
        name: Adobe Sign
      - aid: adp-wisely
        url: https://app.workato.com/browse/recipes?q=app:adp-wisely
        name: Adp Wisely
      - aid: adp-workforce-now
        url: https://app.workato.com/browse/recipes?q=app:adp-workforce-now
        name: Adp Workforce Now
      - aid: adyen
        url: https://app.workato.com/browse/recipes?q=app:adyen
        name: Adyen
      - aid: aftership
        url: https://app.workato.com/browse/recipes?q=app:aftership
        name: AfterShip
      - aid: agiloft
        url: https://app.workato.com/browse/recipes?q=app:agiloft
        name: Agiloft
      - aid: aimtec-clouedi
        url: https://app.workato.com/browse/recipes?q=app:aimtec-clouedi
        name: Aimtec ClouEDI
      - aid: aircall
        url: https://app.workato.com/browse/recipes?q=app:aircall
        name: Aircall
      - aid: akamai-eaa
        url: https://app.workato.com/browse/recipes?q=app:akamai-eaa
        name: Akamai EAA
      - aid: akeneo
        url: https://app.workato.com/browse/recipes?q=app:akeneo
        name: Akeneo
      - aid: alfresco-content-services
        url: https://app.workato.com/browse/recipes?q=app:alfresco-content-services
        name: Alfresco Content Services
      - aid: amazon-cloudwatch
        url: https://app.workato.com/browse/recipes?q=app:amazon-cloudwatch
        name: Amazon CloudWatch
      - aid: amazon-dynamo-db
        url: https://app.workato.com/browse/recipes?q=app:amazon-dynamo-db
        name: Amazon Dynamo DB
      - aid: amazon-inspector2
        url: https://app.workato.com/browse/recipes?q=app:amazon-inspector2
        name: Amazon Inspector2
      - aid: amazon-kinesis
        url: https://app.workato.com/browse/recipes?q=app:amazon-kinesis
        name: Amazon Kinesis
      - aid: amazon-lex
        url: https://app.workato.com/browse/recipes?q=app:amazon-lex
        name: Amazon Lex
      - aid: amazon-sage-maker
        url: https://app.workato.com/browse/recipes?q=app:amazon-sage-maker
        name: Amazon Sage Maker
      - aid: amazon-seller-central
        url: https://app.workato.com/browse/recipes?q=app:amazon-seller-central
        name: Amazon Seller Central
      - aid: amazon-ses
        url: https://app.workato.com/browse/recipes?q=app:amazon-ses
        name: Amazon SES
      - aid: amplify
        url: https://app.workato.com/browse/recipes?q=app:amplify
        name: Amplify
      - aid: anonyflow
        url: https://app.workato.com/browse/recipes?q=app:anonyflow
        name: AnonyFlow
      - aid: anthropic
        url: https://app.workato.com/browse/recipes?q=app:anthropic
        name: Anthropic
      - aid: anvyl
        url: https://app.workato.com/browse/recipes?q=app:anvyl
        name: Anvyl
      - aid: api-void
        url: https://app.workato.com/browse/recipes?q=app:api-void
        name: Api Void
      - aid: apod
        url: https://app.workato.com/browse/recipes?q=app:apod
        name: APOD
      - aid: apollo.io
        url: https://app.workato.com/browse/recipes?q=app:apollo.io
        name: Apollo.io
      - aid: appdirect
        url: https://app.workato.com/browse/recipes?q=app:appdirect
        name: AppDirect
      - aid: applaud
        url: https://app.workato.com/browse/recipes?q=app:applaud
        name: Applaud
      - aid: app-store-connect
        url: https://app.workato.com/browse/recipes?q=app:app-store-connect
        name: App Store Connect
      - aid: appviewx
        url: https://app.workato.com/browse/recipes?q=app:appviewx
        name: AppViewX
      - aid: apromore
        url: https://app.workato.com/browse/recipes?q=app:apromore
        name: Apromore
      - aid: arcanum
        url: https://app.workato.com/browse/recipes?q=app:arcanum
        name: Arcanum
      - aid: ashby
        url: https://app.workato.com/browse/recipes?q=app:ashby
        name: Ashby
      - aid: aspera-on-cloud
        url: https://app.workato.com/browse/recipes?q=app:aspera-on-cloud
        name: Aspera on Cloud
      - aid: astra
        url: https://app.workato.com/browse/recipes?q=app:astra
        name: Astra
      - aid: astrix
        url: https://app.workato.com/browse/recipes?q=app:astrix
        name: Astrix
      - aid: auth0
        url: https://app.workato.com/browse/recipes?q=app:auth0
        name: Auth0
      - aid: autodesk-construction-cloud-(public-beta)
        url: https://app.workato.com/browse/recipes?q=app:autodesk-construction-cloud-(public-beta)
        name: Autodesk Construction Cloud (Public Beta)
      - aid: automation-anywhere
        url: https://app.workato.com/browse/recipes?q=app:automation-anywhere
        name: Automation Anywhere
      - aid: awardco
        url: https://app.workato.com/browse/recipes?q=app:awardco
        name: Awardco
      - aid: aws-api-gateway
        url: https://app.workato.com/browse/recipes?q=app:aws-api-gateway
        name: AWS API Gateway
      - aid: aws-athena
        url: https://app.workato.com/browse/recipes?q=app:aws-athena
        name: AWS Athena
      - aid: aws-bedrock
        url: https://app.workato.com/browse/recipes?q=app:aws-bedrock
        name: AWS Bedrock
      - aid: aws-detective
        url: https://app.workato.com/browse/recipes?q=app:aws-detective
        name: AWS Detective
      - aid: aws-guardduty
        url: https://app.workato.com/browse/recipes?q=app:aws-guardduty
        name: AWS GuardDuty
      - aid: aws-key-management-service
        url: https://app.workato.com/browse/recipes?q=app:aws-key-management-service
        name: AWS Key Management Service
      - aid: aws-product-advertising
        url: https://app.workato.com/browse/recipes?q=app:aws-product-advertising
        name: AWS Product Advertising
      - aid: aws-secrets-manager
        url: https://app.workato.com/browse/recipes?q=app:aws-secrets-manager
        name: AWS Secrets Manager
      - aid: aws-security-hub
        url: https://app.workato.com/browse/recipes?q=app:aws-security-hub
        name: AWS Security Hub
      - aid: azure-active-directory
        url: https://app.workato.com/browse/recipes?q=app:azure-active-directory
        name: Azure Active Directory
      - aid: azure-devops
        url: https://app.workato.com/browse/recipes?q=app:azure-devops
        name: Azure DevOps
      - aid: azure-form-recognizer
        url: https://app.workato.com/browse/recipes?q=app:azure-form-recognizer
        name: Azure Form Recognizer
      - aid: azure-sentinel
        url: https://app.workato.com/browse/recipes?q=app:azure-sentinel
        name: Azure Sentinel
      - aid: azure-service-bus
        url: https://app.workato.com/browse/recipes?q=app:azure-service-bus
        name: Azure Service Bus
      - aid: backlog
        url: https://app.workato.com/browse/recipes?q=app:backlog
        name: Backlog
      - aid: bakuraku-()
        url: https://app.workato.com/browse/recipes?q=app:bakuraku-()
        name: Bakuraku ()
      - aid: barista
        url: https://app.workato.com/browse/recipes?q=app:barista
        name: Barista
      - aid: beaconstac
        url: https://app.workato.com/browse/recipes?q=app:beaconstac
        name: Beaconstac
      - aid: benchling
        url: https://app.workato.com/browse/recipes?q=app:benchling
        name: Benchling
      - aid: big-commerce
        url: https://app.workato.com/browse/recipes?q=app:big-commerce
        name: Big Commerce
      - aid: biotime
        url: https://app.workato.com/browse/recipes?q=app:biotime
        name: biotime
      - aid: birdview-psa
        url: https://app.workato.com/browse/recipes?q=app:birdview-psa
        name: Birdview PSA
      - aid: bitlocker
        url: https://app.workato.com/browse/recipes?q=app:bitlocker
        name: Bitlocker
      - aid: biz-gate
        url: https://app.workato.com/browse/recipes?q=app:biz-gate
        name: Biz Gate
      - aid: bizzabo
        url: https://app.workato.com/browse/recipes?q=app:bizzabo
        name: Bizzabo
      - aid: blackline
        url: https://app.workato.com/browse/recipes?q=app:blackline
        name: BlackLine
      - aid: blackline-reports
        url: https://app.workato.com/browse/recipes?q=app:blackline-reports
        name: BlackLine Reports
      - aid: bloomfire
        url: https://app.workato.com/browse/recipes?q=app:bloomfire
        name: Bloomfire
      - aid: bluepoint
        url: https://app.workato.com/browse/recipes?q=app:bluepoint
        name: Bluepoint
      - aid: bmc-helix-itsm
        url: https://app.workato.com/browse/recipes?q=app:bmc-helix-itsm
        name: BMC Helix ITSM
      - aid: bmc-innovation-suite
        url: https://app.workato.com/browse/recipes?q=app:bmc-innovation-suite
        name: BMC Innovation Suite
      - aid: breeze
        url: https://app.workato.com/browse/recipes?q=app:breeze
        name: Breeze
      - aid: brex
        url: https://app.workato.com/browse/recipes?q=app:brex
        name: Brex
      - aid: buildingconnected
        url: https://app.workato.com/browse/recipes?q=app:buildingconnected
        name: BuildingConnected
      - aid: buildxact
        url: https://app.workato.com/browse/recipes?q=app:buildxact
        name: BuildXact
      - aid: calendly
        url: https://app.workato.com/browse/recipes?q=app:calendly
        name: Calendly
      - aid: campaign-cleaner
        url: https://app.workato.com/browse/recipes?q=app:campaign-cleaner
        name: Campaign Cleaner
      - aid: campaign-monitor
        url: https://app.workato.com/browse/recipes?q=app:campaign-monitor
        name: Campaign Monitor
      - aid: camplife
        url: https://app.workato.com/browse/recipes?q=app:camplife
        name: Camplife
      - aid: canva
        url: https://app.workato.com/browse/recipes?q=app:canva
        name: Canva
      - aid: canvas-lms
        url: https://app.workato.com/browse/recipes?q=app:canvas-lms
        name: Canvas LMS
      - aid: capsule-crm
        url: https://app.workato.com/browse/recipes?q=app:capsule-crm
        name: Capsule CRM
      - aid: carbone
        url: https://app.workato.com/browse/recipes?q=app:carbone
        name: Carbone
      - aid: casavi
        url: https://app.workato.com/browse/recipes?q=app:casavi
        name: Casavi
      - aid: caspio
        url: https://app.workato.com/browse/recipes?q=app:caspio
        name: Caspio
      - aid: centric-connector
        url: https://app.workato.com/browse/recipes?q=app:centric-connector
        name: Centric Connector
      - aid: ceridian-dayforce
        url: https://app.workato.com/browse/recipes?q=app:ceridian-dayforce
        name: Ceridian Dayforce
      - aid: cerner
        url: https://app.workato.com/browse/recipes?q=app:cerner
        name: Cerner
      - aid: channelengine
        url: https://app.workato.com/browse/recipes?q=app:channelengine
        name: ChannelEngine
      - aid: chargebee
        url: https://app.workato.com/browse/recipes?q=app:chargebee
        name: Chargebee
      - aid: chart-mogul
        url: https://app.workato.com/browse/recipes?q=app:chart-mogul
        name: Chart Mogul
      - aid: checkr
        url: https://app.workato.com/browse/recipes?q=app:checkr
        name: Checkr
      - aid: chili-piper
        url: https://app.workato.com/browse/recipes?q=app:chili-piper
        name: Chili Piper
      - aid: cicd
        url: https://app.workato.com/browse/recipes?q=app:cicd
        name: CICD
      - aid: circa
        url: https://app.workato.com/browse/recipes?q=app:circa
        name: Circa
      - aid: cisco-amp
        url: https://app.workato.com/browse/recipes?q=app:cisco-amp
        name: Cisco Amp
      - aid: cisco-meraki
        url: https://app.workato.com/browse/recipes?q=app:cisco-meraki
        name: Cisco Meraki
      - aid: cisco-threat-response
        url: https://app.workato.com/browse/recipes?q=app:cisco-threat-response
        name: Cisco Threat Response
      - aid: cisco-umbrella
        url: https://app.workato.com/browse/recipes?q=app:cisco-umbrella
        name: Cisco Umbrella
      - aid: cisco-webex-meetings
        url: https://app.workato.com/browse/recipes?q=app:cisco-webex-meetings
        name: Cisco Webex Meetings
      - aid: citeline
        url: https://app.workato.com/browse/recipes?q=app:citeline
        name: Citeline
      - aid: citrix-right-signature
        url: https://app.workato.com/browse/recipes?q=app:citrix-right-signature
        name: Citrix Right Signature
      - aid: citrix-sharefile
        url: https://app.workato.com/browse/recipes?q=app:citrix-sharefile
        name: Citrix Sharefile
      - aid: clari
        url: https://app.workato.com/browse/recipes?q=app:clari
        name: Clari
      - aid: clarizen-go
        url: https://app.workato.com/browse/recipes?q=app:clarizen-go
        name: Clarizen Go
      - aid: clarizen-one
        url: https://app.workato.com/browse/recipes?q=app:clarizen-one
        name: Clarizen One
      - aid: classy
        url: https://app.workato.com/browse/recipes?q=app:classy
        name: Classy
      - aid: clicksend-sms
        url: https://app.workato.com/browse/recipes?q=app:clicksend-sms
        name: ClickSend SMS
      - aid: clickup
        url: https://app.workato.com/browse/recipes?q=app:clickup
        name: ClickUp
      - aid: cloudblue-marketplace
        url: https://app.workato.com/browse/recipes?q=app:cloudblue-marketplace
        name: CloudBlue Marketplace
      - aid: cloudblue-subscription-management
        url: https://app.workato.com/browse/recipes?q=app:cloudblue-subscription-management
        name: CloudBlue Subscription Management
      - aid: cloud-bot
        url: https://app.workato.com/browse/recipes?q=app:cloud-bot
        name: Cloud BOT
      - aid: cloudconvert
        url: https://app.workato.com/browse/recipes?q=app:cloudconvert
        name: cloudconvert
      - aid: cloudinary
        url: https://app.workato.com/browse/recipes?q=app:cloudinary
        name: Cloudinary
      - aid: cloud-sign
        url: https://app.workato.com/browse/recipes?q=app:cloud-sign
        name: Cloud Sign
      - aid: clover
        url: https://app.workato.com/browse/recipes?q=app:clover
        name: Clover
      - aid: coax
        url: https://app.workato.com/browse/recipes?q=app:coax
        name: Coax
      - aid: cobalt
        url: https://app.workato.com/browse/recipes?q=app:cobalt
        name: Cobalt
      - aid: cobblestone-contract-management-software
        url: https://app.workato.com/browse/recipes?q=app:cobblestone-contract-management-software
        name: Cobblestone Contract Management Software
      - aid: cobee
        url: https://app.workato.com/browse/recipes?q=app:cobee
        name: Cobee
      - aid: code42-incydr
        url: https://app.workato.com/browse/recipes?q=app:code42-incydr
        name: Code42 Incydr
      - aid: codility
        url: https://app.workato.com/browse/recipes?q=app:codility
        name: Codility
      - aid: collibra-data-intelligence-cloud
        url: https://app.workato.com/browse/recipes?q=app:collibra-data-intelligence-cloud
        name: Collibra Data Intelligence Cloud
      - aid: companies-house
        url: https://app.workato.com/browse/recipes?q=app:companies-house
        name: Companies House
      - aid: complete-edi-solutions
        url: https://app.workato.com/browse/recipes?q=app:complete-edi-solutions
        name: Complete EDI Solutions
      - aid: conga-composer
        url: https://app.workato.com/browse/recipes?q=app:conga-composer
        name: Conga Composer
      - aid: connect-wise
        url: https://app.workato.com/browse/recipes?q=app:connect-wise
        name: Connect Wise
      - aid: consensus
        url: https://app.workato.com/browse/recipes?q=app:consensus
        name: Consensus
      - aid: constant-contact
        url: https://app.workato.com/browse/recipes?q=app:constant-contact
        name: Constant Contact
      - aid: contentsquare
        url: https://app.workato.com/browse/recipes?q=app:contentsquare
        name: Contentsquare
      - aid: contentstack
        url: https://app.workato.com/browse/recipes?q=app:contentstack
        name: Contentstack
      - aid: contracts-clm
        url: https://app.workato.com/browse/recipes?q=app:contracts-clm
        name: ContractS CLM
      - aid: contracts-clm-api-v2
        url: https://app.workato.com/browse/recipes?q=app:contracts-clm-api-v2
        name: ContractS CLM API v2
      - aid: convertapi
        url: https://app.workato.com/browse/recipes?q=app:convertapi
        name: ConvertAPI
      - aid: copper
        url: https://app.workato.com/browse/recipes?q=app:copper
        name: Copper
      - aid: cornerstone-hr
        url: https://app.workato.com/browse/recipes?q=app:cornerstone-hr
        name: Cornerstone HR
      - aid: couchbase-capella
        url: https://app.workato.com/browse/recipes?q=app:couchbase-capella
        name: Couchbase Capella
      - aid: coupa-hiperos
        url: https://app.workato.com/browse/recipes?q=app:coupa-hiperos
        name: Coupa Hiperos
      - aid: covertapi
        url: https://app.workato.com/browse/recipes?q=app:covertapi
        name: CovertAPI
      - aid: creatio
        url: https://app.workato.com/browse/recipes?q=app:creatio
        name: Creatio
      - aid: credly
        url: https://app.workato.com/browse/recipes?q=app:credly
        name: Credly
      - aid: crelate
        url: https://app.workato.com/browse/recipes?q=app:crelate
        name: Crelate
      - aid: crossbeam
        url: https://app.workato.com/browse/recipes?q=app:crossbeam
        name: Crossbeam
      - aid: crowdstrike-falcon
        url: https://app.workato.com/browse/recipes?q=app:crowdstrike-falcon
        name: CrowdStrike Falcon
      - aid: cupixworks
        url: https://app.workato.com/browse/recipes?q=app:cupixworks
        name: CupixWorks
      - aid: cvent
        url: https://app.workato.com/browse/recipes?q=app:cvent
        name: Cvent
      - aid: cybelangel
        url: https://app.workato.com/browse/recipes?q=app:cybelangel
        name: CybelAngel
      - aid: cyberark-identity
        url: https://app.workato.com/browse/recipes?q=app:cyberark-identity
        name: CyberArk Identity
      - aid: cybersource
        url: https://app.workato.com/browse/recipes?q=app:cybersource
        name: Cybersource
      - aid: cypher-learning
        url: https://app.workato.com/browse/recipes?q=app:cypher-learning
        name: Cypher Learning
      - aid: d2l-brightspace
        url: https://app.workato.com/browse/recipes?q=app:d2l-brightspace
        name: D2L Brightspace
      - aid: d7sms
        url: https://app.workato.com/browse/recipes?q=app:d7sms
        name: D7SMS
      - aid: data247.com
        url: https://app.workato.com/browse/recipes?q=app:data247.com
        name: Data247.Com
      - aid: datacom-easipay
        url: https://app.workato.com/browse/recipes?q=app:datacom-easipay
        name: Datacom Easipay
      - aid: datadog
        url: https://app.workato.com/browse/recipes?q=app:datadog
        name: Datadog
      - aid: datev-data-services
        url: https://app.workato.com/browse/recipes?q=app:datev-data-services
        name: DATEV Data Services
      - aid: dbt-cloud
        url: https://app.workato.com/browse/recipes?q=app:dbt-cloud
        name: dbt Cloud
      - aid: deal-cloud
        url: https://app.workato.com/browse/recipes?q=app:deal-cloud
        name: Deal Cloud
      - aid: deepl
        url: https://app.workato.com/browse/recipes?q=app:deepl
        name: DeepL
      - aid: deepseek
        url: https://app.workato.com/browse/recipes?q=app:deepseek
        name: DeepSeek
      - aid: delta-lake
        url: https://app.workato.com/browse/recipes?q=app:delta-lake
        name: Delta Lake
      - aid: deltek-maconomy
        url: https://app.workato.com/browse/recipes?q=app:deltek-maconomy
        name: Deltek Maconomy
      - aid: deltek-talent
        url: https://app.workato.com/browse/recipes?q=app:deltek-talent
        name: Deltek Talent
      - aid: deltek-vantagepoint
        url: https://app.workato.com/browse/recipes?q=app:deltek-vantagepoint
        name: Deltek Vantagepoint
      - aid: demandbase
        url: https://app.workato.com/browse/recipes?q=app:demandbase
        name: Demandbase
      - aid: descartes
        url: https://app.workato.com/browse/recipes?q=app:descartes
        name: Descartes
      - aid: dialogflow-cx
        url: https://app.workato.com/browse/recipes?q=app:dialogflow-cx
        name: Dialogflow CX
      - aid: dirrect-supply
        url: https://app.workato.com/browse/recipes?q=app:dirrect-supply
        name: Dirrect Supply
      - aid: discord
        url: https://app.workato.com/browse/recipes?q=app:discord
        name: Discord
      - aid: discover-org
        url: https://app.workato.com/browse/recipes?q=app:discover-org
        name: Discover Org
      - aid: dispatch
        url: https://app.workato.com/browse/recipes?q=app:dispatch
        name: Dispatch
      - aid: domo
        url: https://app.workato.com/browse/recipes?q=app:domo
        name: DOMO
      - aid: doubleclick
        url: https://app.workato.com/browse/recipes?q=app:doubleclick
        name: Doubleclick
      - aid: drift
        url: https://app.workato.com/browse/recipes?q=app:drift
        name: Drift
      - aid: dropthought
        url: https://app.workato.com/browse/recipes?q=app:dropthought
        name: DropThought
      - aid: duco
        url: https://app.workato.com/browse/recipes?q=app:duco
        name: Duco
      - aid: dun-and-bradstreet
        url: https://app.workato.com/browse/recipes?q=app:dun-and-bradstreet
        name: Dun and Bradstreet
      - aid: duocircle
        url: https://app.workato.com/browse/recipes?q=app:duocircle
        name: DuoCircle
      - aid: duo-security
        url: https://app.workato.com/browse/recipes?q=app:duo-security
        name: Duo Security
      - aid: d.vinci
        url: https://app.workato.com/browse/recipes?q=app:d.vinci
        name: d.vinci
      - aid: dx-suite
        url: https://app.workato.com/browse/recipes?q=app:dx-suite
        name: DX Suite
      - aid: easypost
        url: https://app.workato.com/browse/recipes?q=app:easypost
        name: EasyPost
      - aid: ecologi
        url: https://app.workato.com/browse/recipes?q=app:ecologi
        name: Ecologi
      - aid: edcast
        url: https://app.workato.com/browse/recipes?q=app:edcast
        name: EdCast
      - aid: efront
        url: https://app.workato.com/browse/recipes?q=app:efront
        name: eFront
      - aid: e-gov
        url: https://app.workato.com/browse/recipes?q=app:e-gov
        name: e-Gov
      - aid: eido
        url: https://app.workato.com/browse/recipes?q=app:eido
        name: EIDO
      - aid: elasticsearch
        url: https://app.workato.com/browse/recipes?q=app:elasticsearch
        name: Elasticsearch
      - aid: ellucian-colleague-web-apis
        url: https://app.workato.com/browse/recipes?q=app:ellucian-colleague-web-apis
        name: Ellucian Colleague Web APIs
      - aid: email-(custom)
        url: https://app.workato.com/browse/recipes?q=app:email-(custom)
        name: Email (Custom)
      - aid: emaint-x5
        url: https://app.workato.com/browse/recipes?q=app:emaint-x5
        name: eMaint X5
      - aid: employment-hero
        url: https://app.workato.com/browse/recipes?q=app:employment-hero
        name: Employment Hero
      - aid: envoy
        url: https://app.workato.com/browse/recipes?q=app:envoy
        name: Envoy
      - aid: ephesoft-transact
        url: https://app.workato.com/browse/recipes?q=app:ephesoft-transact
        name: Ephesoft Transact
      - aid: epic
        url: https://app.workato.com/browse/recipes?q=app:epic
        name: Epic
      - aid: equipme
        url: https://app.workato.com/browse/recipes?q=app:equipme
        name: equipme
      - aid: evisort
        url: https://app.workato.com/browse/recipes?q=app:evisort
        name: Evisort
      - aid: exact-online
        url: https://app.workato.com/browse/recipes?q=app:exact-online
        name: Exact Online
      - aid: facebook-marketing
        url: https://app.workato.com/browse/recipes?q=app:facebook-marketing
        name: Facebook Marketing
      - aid: facebook-page-management
        url: https://app.workato.com/browse/recipes?q=app:facebook-page-management
        name: Facebook Page Management
      - aid: fedex
        url: https://app.workato.com/browse/recipes?q=app:fedex
        name: FedEx
      - aid: fhir
        url: https://app.workato.com/browse/recipes?q=app:fhir
        name: FHIR
      - aid: flat-file-database
        url: https://app.workato.com/browse/recipes?q=app:flat-file-database
        name: Flat file database
      - aid: floki-health
        url: https://app.workato.com/browse/recipes?q=app:floki-health
        name: FloKi Health
      - aid: fonedynamics
        url: https://app.workato.com/browse/recipes?q=app:fonedynamics
        name: FoneDynamics
      - aid: foqal
        url: https://app.workato.com/browse/recipes?q=app:foqal
        name: Foqal
      - aid: form-assembly
        url: https://app.workato.com/browse/recipes?q=app:form-assembly
        name: Form Assembly
      - aid: formstack-documents
        url: https://app.workato.com/browse/recipes?q=app:formstack-documents
        name: Formstack Documents
      - aid: foundu
        url: https://app.workato.com/browse/recipes?q=app:foundu
        name: foundU
      - aid: fountain
        url: https://app.workato.com/browse/recipes?q=app:fountain
        name: Fountain
      - aid: freee
        url: https://app.workato.com/browse/recipes?q=app:freee
        name: freee
      - aid: freee
        url: https://app.workato.com/browse/recipes?q=app:freee
        name: freee
      - aid: freeeB
        url: https://app.workato.com/browse/recipes?q=app:freeeB
        name: freeeB
      - aid: freshchat
        url: https://app.workato.com/browse/recipes?q=app:freshchat
        name: Freshchat
      - aid: freshdesk
        url: https://app.workato.com/browse/recipes?q=app:freshdesk
        name: Freshdesk
      - aid: freshsales
        url: https://app.workato.com/browse/recipes?q=app:freshsales
        name: Freshsales
      - aid: freshservice
        url: https://app.workato.com/browse/recipes?q=app:freshservice
        name: Freshservice
      - aid: front
        url: https://app.workato.com/browse/recipes?q=app:front
        name: Front
      - aid: fullstory
        url: https://app.workato.com/browse/recipes?q=app:fullstory
        name: Fullstory
      - aid: gainsight
        url: https://app.workato.com/browse/recipes?q=app:gainsight
        name: Gainsight
      - aid: gender-api
        url: https://app.workato.com/browse/recipes?q=app:gender-api
        name: Gender Api
      - aid: getaccept
        url: https://app.workato.com/browse/recipes?q=app:getaccept
        name: GetAccept
      - aid: gitlab
        url: https://app.workato.com/browse/recipes?q=app:gitlab
        name: Gitlab
      - aid: glean
        url: https://app.workato.com/browse/recipes?q=app:glean
        name: Glean
      - aid: globalmeet-webcast
        url: https://app.workato.com/browse/recipes?q=app:globalmeet-webcast
        name: GlobalMeet Webcast
      - aid: gocanvas
        url: https://app.workato.com/browse/recipes?q=app:gocanvas
        name: GoCanvas
      - aid: goco
        url: https://app.workato.com/browse/recipes?q=app:goco
        name: GoCo
      - aid: google-ads
        url: https://app.workato.com/browse/recipes?q=app:google-ads
        name: Google Ads
      - aid: google-analytics
        url: https://app.workato.com/browse/recipes?q=app:google-analytics
        name: Google Analytics
      - aid: google-chat
        url: https://app.workato.com/browse/recipes?q=app:google-chat
        name: Google Chat
      - aid: google-cloud-functions
        url: https://app.workato.com/browse/recipes?q=app:google-cloud-functions
        name: Google Cloud Functions
      - aid: google-docs
        url: https://app.workato.com/browse/recipes?q=app:google-docs
        name: Google Docs
      - aid: google-document-ai
        url: https://app.workato.com/browse/recipes?q=app:google-document-ai
        name: Google Document AI
      - aid: google-drive-(custom)
        url: https://app.workato.com/browse/recipes?q=app:google-drive-(custom)
        name: Google Drive (Custom)
      - aid: google-enterprise-licence-manager
        url: https://app.workato.com/browse/recipes?q=app:google-enterprise-licence-manager
        name: Google Enterprise Licence Manager
      - aid: google-forms
        url: https://app.workato.com/browse/recipes?q=app:google-forms
        name: Google Forms
      - aid: google-gemini
        url: https://app.workato.com/browse/recipes?q=app:google-gemini
        name: Google Gemini
      - aid: google-meet
        url: https://app.workato.com/browse/recipes?q=app:google-meet
        name: Google Meet
      - aid: google-natural-language
        url: https://app.workato.com/browse/recipes?q=app:google-natural-language
        name: Google Natural Language
      - aid: google-pubsub
        url: https://app.workato.com/browse/recipes?q=app:google-pubsub
        name: Google PubSub
      - aid: google-safe-browsing
        url: https://app.workato.com/browse/recipes?q=app:google-safe-browsing
        name: Google Safe Browsing
      - aid: google-slides
        url: https://app.workato.com/browse/recipes?q=app:google-slides
        name: Google Slides
      - aid: google-suite-admin
        url: https://app.workato.com/browse/recipes?q=app:google-suite-admin
        name: Google Suite Admin
      - aid: google-vault
        url: https://app.workato.com/browse/recipes?q=app:google-vault
        name: Google Vault
      - aid: google-vertex-ai
        url: https://app.workato.com/browse/recipes?q=app:google-vertex-ai
        name: Google Vertex AI
      - aid: graphql
        url: https://app.workato.com/browse/recipes?q=app:graphql
        name: GraphQL
      - aid: gravity-forms
        url: https://app.workato.com/browse/recipes?q=app:gravity-forms
        name: Gravity Forms
      - aid: guidecx
        url: https://app.workato.com/browse/recipes?q=app:guidecx
        name: GUIDEcx
      - aid: guru
        url: https://app.workato.com/browse/recipes?q=app:guru
        name: Guru
      - aid: gusto
        url: https://app.workato.com/browse/recipes?q=app:gusto
        name: Gusto
      - aid: harvest
        url: https://app.workato.com/browse/recipes?q=app:harvest
        name: Harvest
      - aid: hello-sign
        url: https://app.workato.com/browse/recipes?q=app:hello-sign
        name: Hello Sign
      - aid: herohealth
        url: https://app.workato.com/browse/recipes?q=app:herohealth
        name: HeroHealth
      - aid: heymarket
        url: https://app.workato.com/browse/recipes?q=app:heymarket
        name: HeyMarket
      - aid: hibob
        url: https://app.workato.com/browse/recipes?q=app:hibob
        name: HiBob
      - aid: highspot
        url: https://app.workato.com/browse/recipes?q=app:highspot
        name: Highspot
      - aid: hl7
        url: https://app.workato.com/browse/recipes?q=app:hl7
        name: HL7
      - aid: hopin
        url: https://app.workato.com/browse/recipes?q=app:hopin
        name: Hopin
      - aid: hotelkey
        url: https://app.workato.com/browse/recipes?q=app:hotelkey
        name: HotelKey
      - aid: hreasilypro
        url: https://app.workato.com/browse/recipes?q=app:hreasilypro
        name: HReasilyPro
      - aid: hr-flow.ai
        url: https://app.workato.com/browse/recipes?q=app:hr-flow.ai
        name: Hr Flow.Ai
      - aid: hr-partner
        url: https://app.workato.com/browse/recipes?q=app:hr-partner
        name: HR Partner
      - aid: hubspot
        url: https://app.workato.com/browse/recipes?q=app:hubspot
        name: HubSpot
      - aid: hunter.io
        url: https://app.workato.com/browse/recipes?q=app:hunter.io
        name: Hunter.io
      - aid: ichris
        url: https://app.workato.com/browse/recipes?q=app:ichris
        name: ichris
      - aid: ichris-(dynamic)
        url: https://app.workato.com/browse/recipes?q=app:ichris-(dynamic)
        name: iChris (Dynamic)
      - aid: ichris-(static)
        url: https://app.workato.com/browse/recipes?q=app:ichris-(static)
        name: iChris (Static)
      - aid: ilevel
        url: https://app.workato.com/browse/recipes?q=app:ilevel
        name: iLevel
      - aid: infobip
        url: https://app.workato.com/browse/recipes?q=app:infobip
        name: Infobip
      - aid: infor-talent-management
        url: https://app.workato.com/browse/recipes?q=app:infor-talent-management
        name: Infor Talent Management
      - aid: inriver
        url: https://app.workato.com/browse/recipes?q=app:inriver
        name: Inriver
      - aid: inriver-pim
        url: https://app.workato.com/browse/recipes?q=app:inriver-pim
        name: inRiver PIM
      - aid: insided
        url: https://app.workato.com/browse/recipes?q=app:insided
        name: Insided
      - aid: insider
        url: https://app.workato.com/browse/recipes?q=app:insider
        name: Insider
      - aid: insightvm
        url: https://app.workato.com/browse/recipes?q=app:insightvm
        name: InsightVM
      - aid: instabase
        url: https://app.workato.com/browse/recipes?q=app:instabase
        name: Instabase
      - aid: intellum-platform
        url: https://app.workato.com/browse/recipes?q=app:intellum-platform
        name: Intellum Platform
      - aid: invoiced
        url: https://app.workato.com/browse/recipes?q=app:invoiced
        name: Invoiced
      - aid: iress-xplan
        url: https://app.workato.com/browse/recipes?q=app:iress-xplan
        name: Iress XPLAN
      - aid: iso2handle
        url: https://app.workato.com/browse/recipes?q=app:iso2handle
        name: ISO2HANDLE
      - aid: iterable
        url: https://app.workato.com/browse/recipes?q=app:iterable
        name: Iterable
      - aid: ivanti-neurons
        url: https://app.workato.com/browse/recipes?q=app:ivanti-neurons
        name: Ivanti Neurons
      - aid: jamf
        url: https://app.workato.com/browse/recipes?q=app:jamf
        name: Jamf
      - aid: japan-corporate-numbers
        url: https://app.workato.com/browse/recipes?q=app:japan-corporate-numbers
        name: Japan Corporate Numbers
      - aid: japanese-characters-converter
        url: https://app.workato.com/browse/recipes?q=app:japanese-characters-converter
        name: Japanese characters converter
      - aid: jd-edwards
        url: https://app.workato.com/browse/recipes?q=app:jd-edwards
        name: JD Edwards
      - aid: jha-cif2020
        url: https://app.workato.com/browse/recipes?q=app:jha-cif2020
        name: JHA CIF2020
      - aid: jha-silverlake
        url: https://app.workato.com/browse/recipes?q=app:jha-silverlake
        name: JHA Silverlake
      - aid: jha-symitar
        url: https://app.workato.com/browse/recipes?q=app:jha-symitar
        name: JHA Symitar
      - aid: jha-synergy
        url: https://app.workato.com/browse/recipes?q=app:jha-synergy
        name: JHA Synergy
      - aid: jira-assets
        url: https://app.workato.com/browse/recipes?q=app:jira-assets
        name: Jira Assets
      - aid: jobadder
        url: https://app.workato.com/browse/recipes?q=app:jobadder
        name: JobAdder
      - aid: jobvite-(custom)
        url: https://app.workato.com/browse/recipes?q=app:jobvite-(custom)
        name: Jobvite (Custom)
      - aid: k2-workflow
        url: https://app.workato.com/browse/recipes?q=app:k2-workflow
        name: K2 Workflow
      - aid: kaltura
        url: https://app.workato.com/browse/recipes?q=app:kaltura
        name: Kaltura
      - aid: karte-acount
        url: https://app.workato.com/browse/recipes?q=app:karte-acount
        name: KARTE Acount
      - aid: karte-action
        url: https://app.workato.com/browse/recipes?q=app:karte-action
        name: KARTE Action
      - aid: karte-datahub
        url: https://app.workato.com/browse/recipes?q=app:karte-datahub
        name: Karte Datahub
      - aid: karte-insight
        url: https://app.workato.com/browse/recipes?q=app:karte-insight
        name: Karte Insight
      - aid: karte-proejct
        url: https://app.workato.com/browse/recipes?q=app:karte-proejct
        name: KARTE Proejct
      - aid: kenna-security
        url: https://app.workato.com/browse/recipes?q=app:kenna-security
        name: Kenna Security
      - aid: keycloak
        url: https://app.workato.com/browse/recipes?q=app:keycloak
        name: Keycloak
      - aid: keypay
        url: https://app.workato.com/browse/recipes?q=app:keypay
        name: KeyPay
      - aid: kickflow
        url: https://app.workato.com/browse/recipes?q=app:kickflow
        name: kickflow
      - aid: kintone
        url: https://app.workato.com/browse/recipes?q=app:kintone
        name: Kintone
      - aid: kintone-(lite)
        url: https://app.workato.com/browse/recipes?q=app:kintone-(lite)
        name: Kintone (Lite)
      - aid: kissflow
        url: https://app.workato.com/browse/recipes?q=app:kissflow
        name: Kissflow
      - aid: kite-platform
        url: https://app.workato.com/browse/recipes?q=app:kite-platform
        name: Kite Platform
      - aid: klaviyo
        url: https://app.workato.com/browse/recipes?q=app:klaviyo
        name: Klaviyo
      - aid: klippa-dochorizon
        url: https://app.workato.com/browse/recipes?q=app:klippa-dochorizon
        name: Klippa DocHorizon
      - aid: knak.
        url: https://app.workato.com/browse/recipes?q=app:knak.
        name: knak.
      - aid: knowbe4
        url: https://app.workato.com/browse/recipes?q=app:knowbe4
        name: KnowBe4
      - aid: knowmy
        url: https://app.workato.com/browse/recipes?q=app:knowmy
        name: KnowMy
      - aid: lacework
        url: https://app.workato.com/browse/recipes?q=app:lacework
        name: Lacework
      - aid: lark
        url: https://app.workato.com/browse/recipes?q=app:lark
        name: Lark
      - aid: launchdarkly
        url: https://app.workato.com/browse/recipes?q=app:launchdarkly
        name: LaunchDarkly
      - aid: lazy-dev-asap
        url: https://app.workato.com/browse/recipes?q=app:lazy-dev-asap
        name: lazy-dev-asap
      - aid: ldap
        url: https://app.workato.com/browse/recipes?q=app:ldap
        name: LDAP
      - aid: leadiq-api
        url: https://app.workato.com/browse/recipes?q=app:leadiq-api
        name: LeadIQ API
      - aid: leaflet-app
        url: https://app.workato.com/browse/recipes?q=app:leaflet-app
        name: Leaflet App
      - aid: leapsome
        url: https://app.workato.com/browse/recipes?q=app:leapsome
        name: Leapsome
      - aid: legion
        url: https://app.workato.com/browse/recipes?q=app:legion
        name: Legion
      - aid: lever
        url: https://app.workato.com/browse/recipes?q=app:lever
        name: Lever
      - aid: liferay
        url: https://app.workato.com/browse/recipes?q=app:liferay
        name: Liferay
      - aid: lifx
        url: https://app.workato.com/browse/recipes?q=app:lifx
        name: Lifx
      - aid: line
        url: https://app.workato.com/browse/recipes?q=app:line
        name: LINE
      - aid: linear
        url: https://app.workato.com/browse/recipes?q=app:linear
        name: Linear
      - aid: line-works
        url: https://app.workato.com/browse/recipes?q=app:line-works
        name: LINE WORKS
      - aid: linked2pay
        url: https://app.workato.com/browse/recipes?q=app:linked2pay
        name: linked2pay
      - aid: livechat
        url: https://app.workato.com/browse/recipes?q=app:livechat
        name: Livechat
      - aid: liveperson-knowledge-articles-import
        url: https://app.workato.com/browse/recipes?q=app:liveperson-knowledge-articles-import
        name: Liveperson Knowledge Articles Import
      - aid: lobster
        url: https://app.workato.com/browse/recipes?q=app:lobster
        name: Lobster
      - aid: log-insight
        url: https://app.workato.com/browse/recipes?q=app:log-insight
        name: Log Insight
      - aid: logisense-sdk-10.6+
        url: https://app.workato.com/browse/recipes?q=app:logisense-sdk-10.6+
        name: LogiSense SDK 10.6+
      - aid: looker
        url: https://app.workato.com/browse/recipes?q=app:looker
        name: Looker
      - aid: lookout
        url: https://app.workato.com/browse/recipes?q=app:lookout
        name: Lookout
      - aid: loyjoy
        url: https://app.workato.com/browse/recipes?q=app:loyjoy
        name: LoyJoy
      - aid: loyverse
        url: https://app.workato.com/browse/recipes?q=app:loyverse
        name: Loyverse
      - aid: lucca
        url: https://app.workato.com/browse/recipes?q=app:lucca
        name: Lucca
      - aid: lucidity
        url: https://app.workato.com/browse/recipes?q=app:lucidity
        name: Lucidity
      - aid: lumos
        url: https://app.workato.com/browse/recipes?q=app:lumos
        name: Lumos
      - aid: lusha-connect
        url: https://app.workato.com/browse/recipes?q=app:lusha-connect
        name: Lusha Connect
      - aid: mac-centre-api
        url: https://app.workato.com/browse/recipes?q=app:mac-centre-api
        name: Mac Centre API
      - aid: mailazy
        url: https://app.workato.com/browse/recipes?q=app:mailazy
        name: Mailazy
      - aid: mastercard
        url: https://app.workato.com/browse/recipes?q=app:mastercard
        name: MasterCard
      - aid: mattermost
        url: https://app.workato.com/browse/recipes?q=app:mattermost
        name: Mattermost
      - aid: medallia-experience-cloud
        url: https://app.workato.com/browse/recipes?q=app:medallia-experience-cloud
        name: Medallia Experience Cloud
      - aid: me-learning
        url: https://app.workato.com/browse/recipes?q=app:me-learning
        name: Me Learning
      - aid: memsource
        url: https://app.workato.com/browse/recipes?q=app:memsource
        name: Memsource
      - aid: mendix
        url: https://app.workato.com/browse/recipes?q=app:mendix
        name: Mendix
      - aid: message-validator
        url: https://app.workato.com/browse/recipes?q=app:message-validator
        name: Message Validator
      - aid: metabase
        url: https://app.workato.com/browse/recipes?q=app:metabase
        name: Metabase
      - aid: metriport
        url: https://app.workato.com/browse/recipes?q=app:metriport
        name: Metriport
      - aid: metro
        url: https://app.workato.com/browse/recipes?q=app:metro
        name: Metro
      - aid: metronome
        url: https://app.workato.com/browse/recipes?q=app:metronome
        name: Metronome
      - aid: microsoft-advertising
        url: https://app.workato.com/browse/recipes?q=app:microsoft-advertising
        name: Microsoft Advertising
      - aid: microsoft-dynamics-business-central
        url: https://app.workato.com/browse/recipes?q=app:microsoft-dynamics-business-central
        name: Microsoft Dynamics Business Central
      - aid: microsoft-dynamics-finance-and-operations
        url: https://app.workato.com/browse/recipes?q=app:microsoft-dynamics-finance-and-operations
        name: Microsoft Dynamics Finance And Operations
      - aid: microsoft-dynamics-great-plains
        url: https://app.workato.com/browse/recipes?q=app:microsoft-dynamics-great-plains
        name: Microsoft Dynamics Great Plains
      - aid: microsoft-fabric
        url: https://app.workato.com/browse/recipes?q=app:microsoft-fabric
        name: Microsoft Fabric
      - aid: microsoft-graph-api
        url: https://app.workato.com/browse/recipes?q=app:microsoft-graph-api
        name: Microsoft Graph Api
      - aid: microsoft-log-analytics
        url: https://app.workato.com/browse/recipes?q=app:microsoft-log-analytics
        name: Microsoft Log Analytics
      - aid: microsoft-office-365-management-api
        url: https://app.workato.com/browse/recipes?q=app:microsoft-office-365-management-api
        name: Microsoft Office 365 Management Api
      - aid: microsoft-power-bi
        url: https://app.workato.com/browse/recipes?q=app:microsoft-power-bi
        name: Microsoft Power BI
      - aid: mindtickle
        url: https://app.workato.com/browse/recipes?q=app:mindtickle
        name: Mindtickle
      - aid: mistral-ai
        url: https://app.workato.com/browse/recipes?q=app:mistral-ai
        name: Mistral AI
      - aid: monday
        url: https://app.workato.com/browse/recipes?q=app:monday
        name: Monday
      - aid: moveworks
        url: https://app.workato.com/browse/recipes?q=app:moveworks
        name: Moveworks
      - aid: mozilla-observatory
        url: https://app.workato.com/browse/recipes?q=app:mozilla-observatory
        name: Mozilla Observatory
      - aid: mural
        url: https://app.workato.com/browse/recipes?q=app:mural
        name: Mural
      - aid: mvp-one
        url: https://app.workato.com/browse/recipes?q=app:mvp-one
        name: MVP One
      - aid: mx-toolbox
        url: https://app.workato.com/browse/recipes?q=app:mx-toolbox
        name: Mx Toolbox
      - aid: myob-acumatica
        url: https://app.workato.com/browse/recipes?q=app:myob-acumatica
        name: MYOB Acumatica
      - aid: myob-business
        url: https://app.workato.com/browse/recipes?q=app:myob-business
        name: MYOB Business
      - aid: nano-nets
        url: https://app.workato.com/browse/recipes?q=app:nano-nets
        name: Nano Nets
      - aid: navan
        url: https://app.workato.com/browse/recipes?q=app:navan
        name: Navan
      - aid: naver-searchad
        url: https://app.workato.com/browse/recipes?q=app:naver-searchad
        name: Naver SearchAd
      - aid: neo4j-aura
        url: https://app.workato.com/browse/recipes?q=app:neo4j-aura
        name: Neo4j Aura
      - aid: neo4j-desktop
        url: https://app.workato.com/browse/recipes?q=app:neo4j-desktop
        name: Neo4j Desktop
      - aid: nested-data-helper
        url: https://app.workato.com/browse/recipes?q=app:nested-data-helper
        name: Nested Data Helper
      - aid: neto
        url: https://app.workato.com/browse/recipes?q=app:neto
        name: Neto
      - aid: netspi-attack-surface-management
        url: https://app.workato.com/browse/recipes?q=app:netspi-attack-surface-management
        name: NetSPI Attack Surface Management
      - aid: net-suite-open-air
        url: https://app.workato.com/browse/recipes?q=app:net-suite-open-air
        name: Net Suite Open Air
      - aid: netsuite-openair-(rest)
        url: https://app.workato.com/browse/recipes?q=app:netsuite-openair-(rest)
        name: NetSuite OpenAir (REST)
      - aid: neverbounce
        url: https://app.workato.com/browse/recipes?q=app:neverbounce
        name: NeverBounce
      - aid: nhs-electronic-staff-record-(esr)-wrapper
        url: https://app.workato.com/browse/recipes?q=app:nhs-electronic-staff-record-(esr)-wrapper
        name: NHS Electronic Staff Record (ESR) Wrapper
      - aid: nightfall-ai
        url: https://app.workato.com/browse/recipes?q=app:nightfall-ai
        name: Nightfall AI
      - aid: nobb
        url: https://app.workato.com/browse/recipes?q=app:nobb
        name: Nobb
      - aid: nokia-sps
        url: https://app.workato.com/browse/recipes?q=app:nokia-sps
        name: Nokia SPS
      - aid: notion
        url: https://app.workato.com/browse/recipes?q=app:notion
        name: Notion
      - aid: novade
        url: https://app.workato.com/browse/recipes?q=app:novade
        name: Novade
      - aid: nuorder
        url: https://app.workato.com/browse/recipes?q=app:nuorder
        name: NuORDER
      - aid: oanda
        url: https://app.workato.com/browse/recipes?q=app:oanda
        name: Oanda
      - aid: octopus-deploy
        url: https://app.workato.com/browse/recipes?q=app:octopus-deploy
        name: Octopus Deploy
      - aid: odoo
        url: https://app.workato.com/browse/recipes?q=app:odoo
        name: Odoo
      - aid: ollama
        url: https://app.workato.com/browse/recipes?q=app:ollama
        name: Ollama
      - aid: omie
        url: https://app.workato.com/browse/recipes?q=app:omie
        name: Omie
      - aid: onboard
        url: https://app.workato.com/browse/recipes?q=app:onboard
        name: Onboard
      - aid: one-login
        url: https://app.workato.com/browse/recipes?q=app:one-login
        name: One Login
      - aid: onemap-sg
        url: https://app.workato.com/browse/recipes?q=app:onemap-sg
        name: OneMap SG
      - aid: onna
        url: https://app.workato.com/browse/recipes?q=app:onna
        name: Onna
      - aid: openapi
        url: https://app.workato.com/browse/recipes?q=app:openapi
        name: OpenAPI
      - aid: openlegacy
        url: https://app.workato.com/browse/recipes?q=app:openlegacy
        name: Openlegacy
      - aid: openlegacy-hub-connector-
        url: https://app.workato.com/browse/recipes?q=app:openlegacy-hub-connector-
        name: 'OpenLegacy Hub Connector '
      - aid: open-webui
        url: https://app.workato.com/browse/recipes?q=app:open-webui
        name: Open WebUI
      - aid: ops-genie
        url: https://app.workato.com/browse/recipes?q=app:ops-genie
        name: Ops Genie
      - aid: oracle-fusion-cloud-(soap)
        url: https://app.workato.com/browse/recipes?q=app:oracle-fusion-cloud-(soap)
        name: Oracle Fusion Cloud (SOAP)
      - aid: oracle-hdl-file-creator
        url: https://app.workato.com/browse/recipes?q=app:oracle-hdl-file-creator
        name: Oracle HDL file creator
      - aid: orderful
        url: https://app.workato.com/browse/recipes?q=app:orderful
        name: Orderful
      - aid: outlaw
        url: https://app.workato.com/browse/recipes?q=app:outlaw
        name: Outlaw
      - aid: pageup
        url: https://app.workato.com/browse/recipes?q=app:pageup
        name: PageUp
      - aid: pandadoc
        url: https://app.workato.com/browse/recipes?q=app:pandadoc
        name: Pandadoc
      - aid: partnerstack
        url: https://app.workato.com/browse/recipes?q=app:partnerstack
        name: PartnerStack
      - aid: patientsource
        url: https://app.workato.com/browse/recipes?q=app:patientsource
        name: PatientSource
      - aid: payhawk
        url: https://app.workato.com/browse/recipes?q=app:payhawk
        name: Payhawk
      - aid: paylocity
        url: https://app.workato.com/browse/recipes?q=app:paylocity
        name: Paylocity
      - aid: paypal
        url: https://app.workato.com/browse/recipes?q=app:paypal
        name: Paypal
      - aid: pdfmonkey
        url: https://app.workato.com/browse/recipes?q=app:pdfmonkey
        name: PDFMonkey
      - aid: pdm-automotive
        url: https://app.workato.com/browse/recipes?q=app:pdm-automotive
        name: PDM AUTOMOTIVE
      - aid: pega-platform
        url: https://app.workato.com/browse/recipes?q=app:pega-platform
        name: Pega Platform
      - aid: pendo
        url: https://app.workato.com/browse/recipes?q=app:pendo
        name: Pendo
      - aid: peopledoc
        url: https://app.workato.com/browse/recipes?q=app:peopledoc
        name: PeopleDoc
      - aid: percolate-sdk
        url: https://app.workato.com/browse/recipes?q=app:percolate-sdk
        name: Percolate Sdk
      - aid: perplexity
        url: https://app.workato.com/browse/recipes?q=app:perplexity
        name: Perplexity
      - aid: personio
        url: https://app.workato.com/browse/recipes?q=app:personio
        name: Personio
      - aid: pigeonhole-live
        url: https://app.workato.com/browse/recipes?q=app:pigeonhole-live
        name: Pigeonhole Live
      - aid: pigment
        url: https://app.workato.com/browse/recipes?q=app:pigment
        name: Pigment
      - aid: pinecone
        url: https://app.workato.com/browse/recipes?q=app:pinecone
        name: Pinecone
      - aid: pipefy
        url: https://app.workato.com/browse/recipes?q=app:pipefy
        name: Pipefy
      - aid: plentymarkets
        url: https://app.workato.com/browse/recipes?q=app:plentymarkets
        name: Plentymarkets
      - aid: positional-file-tool
        url: https://app.workato.com/browse/recipes?q=app:positional-file-tool
        name: Positional File Tool
      - aid: power-automate-desktop-flow-(rpa)
        url: https://app.workato.com/browse/recipes?q=app:power-automate-desktop-flow-(rpa)
        name: Power Automate Desktop Flow (RPA)
      - aid: priority-software
        url: https://app.workato.com/browse/recipes?q=app:priority-software
        name: Priority Software
      - aid: process-street
        url: https://app.workato.com/browse/recipes?q=app:process-street
        name: Process Street
      - aid: procore
        url: https://app.workato.com/browse/recipes?q=app:procore
        name: Procore
      - aid: qdrant
        url: https://app.workato.com/browse/recipes?q=app:qdrant
        name: Qdrant
      - aid: qualtrics
        url: https://app.workato.com/browse/recipes?q=app:qualtrics
        name: Qualtrics
      - aid: qualys
        url: https://app.workato.com/browse/recipes?q=app:qualys
        name: Qualys
      - aid: quebit-reportworq
        url: https://app.workato.com/browse/recipes?q=app:quebit-reportworq
        name: QueBit ReportWORQ
      - aid: rabbitmq
        url: https://app.workato.com/browse/recipes?q=app:rabbitmq
        name: RabbitMQ
      - aid: raise-custom-error
        url: https://app.workato.com/browse/recipes?q=app:raise-custom-error
        name: Raise Custom Error
      - aid: rally
        url: https://app.workato.com/browse/recipes?q=app:rally
        name: Rally
      - aid: ramp
        url: https://app.workato.com/browse/recipes?q=app:ramp
        name: Ramp
      - aid: redox-engine
        url: https://app.workato.com/browse/recipes?q=app:redox-engine
        name: Redox engine
      - aid: referoo
        url: https://app.workato.com/browse/recipes?q=app:referoo
        name: Referoo
      - aid: reftab
        url: https://app.workato.com/browse/recipes?q=app:reftab
        name: Reftab
      - aid: reltio
        url: https://app.workato.com/browse/recipes?q=app:reltio
        name: Reltio
      - aid: rev-ops
        url: https://app.workato.com/browse/recipes?q=app:rev-ops
        name: Rev Ops
      - aid: rhumbix
        url: https://app.workato.com/browse/recipes?q=app:rhumbix
        name: Rhumbix
      - aid: rhythm-systems
        url: https://app.workato.com/browse/recipes?q=app:rhythm-systems
        name: Rhythm Systems
      - aid: ring-central-video
        url: https://app.workato.com/browse/recipes?q=app:ring-central-video
        name: Ring Central Video
      - aid: risk-cloud
        url: https://app.workato.com/browse/recipes?q=app:risk-cloud
        name: Risk Cloud
      - aid: rocketlane
        url: https://app.workato.com/browse/recipes?q=app:rocketlane
        name: Rocketlane
      - aid: rokt-event-api
        url: https://app.workato.com/browse/recipes?q=app:rokt-event-api
        name: Rokt Event API
      - aid: rossum
        url: https://app.workato.com/browse/recipes?q=app:rossum
        name: Rossum
      - aid: rss
        url: https://app.workato.com/browse/recipes?q=app:rss
        name: RSS
      - aid: safetyculture
        url: https://app.workato.com/browse/recipes?q=app:safetyculture
        name: SafetyCulture
      - aid: sailpoint
        url: https://app.workato.com/browse/recipes?q=app:sailpoint
        name: SailPoint
      - aid: salesforce-data-cloud
        url: https://app.workato.com/browse/recipes?q=app:salesforce-data-cloud
        name: Salesforce Data Cloud
      - aid: salesforce-pardot
        url: https://app.workato.com/browse/recipes?q=app:salesforce-pardot
        name: Salesforce Pardot
      - aid: salesloft
        url: https://app.workato.com/browse/recipes?q=app:salesloft
        name: SalesLoft
      - aid: sansan
        url: https://app.workato.com/browse/recipes?q=app:sansan
        name: Sansan
      - aid: sap-ariba
        url: https://app.workato.com/browse/recipes?q=app:sap-ariba
        name: SAP Ariba
      - aid: sap-business-one
        url: https://app.workato.com/browse/recipes?q=app:sap-business-one
        name: Sap Business One
      - aid: sap-fieldglass
        url: https://app.workato.com/browse/recipes?q=app:sap-fieldglass
        name: SAP Fieldglass
      - aid: sapling-hr
        url: https://app.workato.com/browse/recipes?q=app:sapling-hr
        name: Sapling HR
      - aid: sap-sales-cloud
        url: https://app.workato.com/browse/recipes?q=app:sap-sales-cloud
        name: SAP Sales Cloud
      - aid: sap-successfactors
        url: https://app.workato.com/browse/recipes?q=app:sap-successfactors
        name: SAP SuccessFactors
      - aid: sap-successfactors-lms
        url: https://app.workato.com/browse/recipes?q=app:sap-successfactors-lms
        name: SAP SuccessFactors LMS
      - aid: scinote
        url: https://app.workato.com/browse/recipes?q=app:scinote
        name: SciNote
      - aid: scope-better
        url: https://app.workato.com/browse/recipes?q=app:scope-better
        name: SCOPE Better
      - aid: scout-rfp
        url: https://app.workato.com/browse/recipes?q=app:scout-rfp
        name: Scout Rfp
      - aid: scout-talent-:recruit
        url: https://app.workato.com/browse/recipes?q=app:scout-talent-:recruit
        name: Scout Talent :Recruit
      - aid: seismic
        url: https://app.workato.com/browse/recipes?q=app:seismic
        name: Seismic
      - aid: sendoso
        url: https://app.workato.com/browse/recipes?q=app:sendoso
        name: Sendoso
      - aid: senses
        url: https://app.workato.com/browse/recipes?q=app:senses
        name: Senses
      - aid: sentinel-one
        url: https://app.workato.com/browse/recipes?q=app:sentinel-one
        name: Sentinel One
      - aid: servicedesk-plus
        url: https://app.workato.com/browse/recipes?q=app:servicedesk-plus
        name: ServiceDesk Plus
      - aid: servicenow
        url: https://app.workato.com/browse/recipes?q=app:servicenow
        name: ServiceNow
      - aid: shipmonk
        url: https://app.workato.com/browse/recipes?q=app:shipmonk
        name: Shipmonk
      - aid: ship-station
        url: https://app.workato.com/browse/recipes?q=app:ship-station
        name: Ship Station
      - aid: shipwire
        url: https://app.workato.com/browse/recipes?q=app:shipwire
        name: ShipWire
      - aid: shopware
        url: https://app.workato.com/browse/recipes?q=app:shopware
        name: Shopware
      - aid: sigma
        url: https://app.workato.com/browse/recipes?q=app:sigma
        name: Sigma
      - aid: signavio
        url: https://app.workato.com/browse/recipes?q=app:signavio
        name: Signavio
      - aid: signl4
        url: https://app.workato.com/browse/recipes?q=app:signl4
        name: Signl4
      - aid: sign-request
        url: https://app.workato.com/browse/recipes?q=app:sign-request
        name: Sign Request
      - aid: sinch-sms-&-mms
        url: https://app.workato.com/browse/recipes?q=app:sinch-sms-&-mms
        name: Sinch SMS & MMS
      - aid: singlestore-management
        url: https://app.workato.com/browse/recipes?q=app:singlestore-management
        name: SingleStore Management
      - aid: sirion
        url: https://app.workato.com/browse/recipes?q=app:sirion
        name: Sirion
      - aid: skilljar
        url: https://app.workato.com/browse/recipes?q=app:skilljar
        name: Skilljar
      - aid: skyvern
        url: https://app.workato.com/browse/recipes?q=app:skyvern
        name: Skyvern
      - aid: smartcomm
        url: https://app.workato.com/browse/recipes?q=app:smartcomm
        name: SmartCOMM
      - aid: smart-hr
        url: https://app.workato.com/browse/recipes?q=app:smart-hr
        name: Smart Hr
      - aid: smartpm
        url: https://app.workato.com/browse/recipes?q=app:smartpm
        name: SmartPM
      - aid: smartrecruiters
        url: https://app.workato.com/browse/recipes?q=app:smartrecruiters
        name: SmartRecruiters
      - aid: sms77-sms-&-text2speech-gateway
        url: https://app.workato.com/browse/recipes?q=app:sms77-sms-&-text2speech-gateway
        name: Sms77 Sms & Text2Speech Gateway
      - aid: soap
        url: https://app.workato.com/browse/recipes?q=app:soap
        name: SOAP
      - aid: softools
        url: https://app.workato.com/browse/recipes?q=app:softools
        name: Softools
      - aid: solace
        url: https://app.workato.com/browse/recipes?q=app:solace
        name: Solace
      - aid: sovos
        url: https://app.workato.com/browse/recipes?q=app:sovos
        name: Sovos
      - aid: spotify
        url: https://app.workato.com/browse/recipes?q=app:spotify
        name: Spotify
      - aid: ssl-labs
        url: https://app.workato.com/browse/recipes?q=app:ssl-labs
        name: Ssl Labs
      - aid: stackoverflow
        url: https://app.workato.com/browse/recipes?q=app:stackoverflow
        name: Stackoverflow
      - aid: statuspage
        url: https://app.workato.com/browse/recipes?q=app:statuspage
        name: Statuspage
      - aid: strongbox
        url: https://app.workato.com/browse/recipes?q=app:strongbox
        name: Strongbox
      - aid: submittable
        url: https://app.workato.com/browse/recipes?q=app:submittable
        name: Submittable
      - aid: sugar-crm
        url: https://app.workato.com/browse/recipes?q=app:sugar-crm
        name: Sugar CRM
      - aid: synthesia
        url: https://app.workato.com/browse/recipes?q=app:synthesia
        name: Synthesia
      - aid: tableau
        url: https://app.workato.com/browse/recipes?q=app:tableau
        name: Tableau
      - aid: tadabase
        url: https://app.workato.com/browse/recipes?q=app:tadabase
        name: Tadabase
      - aid: talenox
        url: https://app.workato.com/browse/recipes?q=app:talenox
        name: Talenox
      - aid: talent-palette
        url: https://app.workato.com/browse/recipes?q=app:talent-palette
        name: Talent Palette
      - aid: taleo-(enterprise)
        url: https://app.workato.com/browse/recipes?q=app:taleo-(enterprise)
        name: Taleo (Enterprise)
      - aid: talkdesk
        url: https://app.workato.com/browse/recipes?q=app:talkdesk
        name: Talkdesk
      - aid: tcp-humanity
        url: https://app.workato.com/browse/recipes?q=app:tcp-humanity
        name: TCP Humanity
      - aid: tcp-|-humanity
        url: https://app.workato.com/browse/recipes?q=app:tcp-|-humanity
        name: TCP | Humanity
      - aid: team-dynamix-itsm
        url: https://app.workato.com/browse/recipes?q=app:team-dynamix-itsm
        name: Team Dynamix ITSM
      - aid: teamtailor
        url: https://app.workato.com/browse/recipes?q=app:teamtailor
        name: Teamtailor
      - aid: telegram
        url: https://app.workato.com/browse/recipes?q=app:telegram
        name: Telegram
      - aid: tempo
        url: https://app.workato.com/browse/recipes?q=app:tempo
        name: Tempo
      - aid: tenable
        url: https://app.workato.com/browse/recipes?q=app:tenable
        name: Tenable
      - aid: thankster
        url: https://app.workato.com/browse/recipes?q=app:thankster
        name: Thankster
      - aid: threat-crowd
        url: https://app.workato.com/browse/recipes?q=app:threat-crowd
        name: Threat Crowd
      - aid: threat-miner
        url: https://app.workato.com/browse/recipes?q=app:threat-miner
        name: Threat Miner
      - aid: thriva
        url: https://app.workato.com/browse/recipes?q=app:thriva
        name: Thriva
      - aid: tipalti-approve
        url: https://app.workato.com/browse/recipes?q=app:tipalti-approve
        name: Tipalti Approve
      - aid: todoist
        url: https://app.workato.com/browse/recipes?q=app:todoist
        name: Todoist
      - aid: toggl
        url: https://app.workato.com/browse/recipes?q=app:toggl
        name: Toggl
      - aid: topdesk
        url: https://app.workato.com/browse/recipes?q=app:topdesk
        name: Topdesk
      - aid: torque
        url: https://app.workato.com/browse/recipes?q=app:torque
        name: Torque
      - aid: transmit-sms
        url: https://app.workato.com/browse/recipes?q=app:transmit-sms
        name: Transmit Sms
      - aid: travelperk
        url: https://app.workato.com/browse/recipes?q=app:travelperk
        name: TravelPerk
      - aid: trinet
        url: https://app.workato.com/browse/recipes?q=app:trinet
        name: TriNet
      - aid: trubot-datamatics
        url: https://app.workato.com/browse/recipes?q=app:trubot-datamatics
        name: Trubot Datamatics
      - aid: trustarc-integrations-[winzel]
        url: https://app.workato.com/browse/recipes?q=app:trustarc-integrations-[winzel]
        name: TrustArc Integrations [winzel]
      - aid: trustcruit
        url: https://app.workato.com/browse/recipes?q=app:trustcruit
        name: Trustcruit
      - aid: typeform
        url: https://app.workato.com/browse/recipes?q=app:typeform
        name: Typeform
      - aid: udemy-business
        url: https://app.workato.com/browse/recipes?q=app:udemy-business
        name: Udemy Business
      - aid: uipath
        url: https://app.workato.com/browse/recipes?q=app:uipath
        name: UiPath
      - aid: ukg-dimensions
        url: https://app.workato.com/browse/recipes?q=app:ukg-dimensions
        name: UKG Dimensions
      - aid: ukg-pro
        url: https://app.workato.com/browse/recipes?q=app:ukg-pro
        name: UKG Pro
      - aid: ukg-ready
        url: https://app.workato.com/browse/recipes?q=app:ukg-ready
        name: UKG Ready
      - aid: unshorten.me
        url: https://app.workato.com/browse/recipes?q=app:unshorten.me
        name: Unshorten.Me
      - aid: up-keep
        url: https://app.workato.com/browse/recipes?q=app:up-keep
        name: Up Keep
      - aid: urlscan.io
        url: https://app.workato.com/browse/recipes?q=app:urlscan.io
        name: Urlscan.Io
      - aid: usps
        url: https://app.workato.com/browse/recipes?q=app:usps
        name: USPS
      - aid: utilities
        url: https://app.workato.com/browse/recipes?q=app:utilities
        name: Utilities
      - aid: utmost
        url: https://app.workato.com/browse/recipes?q=app:utmost
        name: Utmost
      - aid: vendorpanel
        url: https://app.workato.com/browse/recipes?q=app:vendorpanel
        name: VendorPanel
      - aid: veza
        url: https://app.workato.com/browse/recipes?q=app:veza
        name: Veza
      - aid: vitally
        url: https://app.workato.com/browse/recipes?q=app:vitally
        name: Vitally
      - aid: walmart-seller-center
        url: https://app.workato.com/browse/recipes?q=app:walmart-seller-center
        name: Walmart Seller Center
      - aid: wasabi
        url: https://app.workato.com/browse/recipes?q=app:wasabi
        name: Wasabi
      - aid: wavity
        url: https://app.workato.com/browse/recipes?q=app:wavity
        name: Wavity
      - aid: webcast-event-management
        url: https://app.workato.com/browse/recipes?q=app:webcast-event-management
        name: Webcast event management
      - aid: weclapp
        url: https://app.workato.com/browse/recipes?q=app:weclapp
        name: weclapp
      - aid: welcome-software
        url: https://app.workato.com/browse/recipes?q=app:welcome-software
        name: Welcome Software
      - aid: welltraq
        url: https://app.workato.com/browse/recipes?q=app:welltraq
        name: WellTraq
      - aid: wistia
        url: https://app.workato.com/browse/recipes?q=app:wistia
        name: Wistia
      - aid: wolken-itsm
        url: https://app.workato.com/browse/recipes?q=app:wolken-itsm
        name: Wolken ITSM
      - aid: woocommerce
        url: https://app.workato.com/browse/recipes?q=app:woocommerce
        name: WooCommerce
      - aid: woodwing-assets
        url: https://app.workato.com/browse/recipes?q=app:woodwing-assets
        name: WoodWing Assets
      - aid: woodwing-studio
        url: https://app.workato.com/browse/recipes?q=app:woodwing-studio
        name: WoodWing Studio
      - aid: workable
        url: https://app.workato.com/browse/recipes?q=app:workable
        name: Workable
      - aid: workato-embedded
        url: https://app.workato.com/browse/recipes?q=app:workato-embedded
        name: Workato Embedded
      - aid: workato-track
        url: https://app.workato.com/browse/recipes?q=app:workato-track
        name: Workato Track
      - aid: workday-(custom)
        url: https://app.workato.com/browse/recipes?q=app:workday-(custom)
        name: Workday (Custom)
      - aid: workday-orchestrate
        url: https://app.workato.com/browse/recipes?q=app:workday-orchestrate
        name: Workday Orchestrate
      - aid: workflow-max
        url: https://app.workato.com/browse/recipes?q=app:workflow-max
        name: Workflow Max
      - aid: workforce
        url: https://app.workato.com/browse/recipes?q=app:workforce
        name: Workforce
      - aid: workpro
        url: https://app.workato.com/browse/recipes?q=app:workpro
        name: WorkPro
      - aid: xemplo
        url: https://app.workato.com/browse/recipes?q=app:xemplo
        name: Xemplo
      - aid: xmatters
        url: https://app.workato.com/browse/recipes?q=app:xmatters
        name: xMatters
      - aid: xml-creator
        url: https://app.workato.com/browse/recipes?q=app:xml-creator
        name: XML Creator
      - aid: xobin
        url: https://app.workato.com/browse/recipes?q=app:xobin
        name: Xobin
      - aid: yarooms
        url: https://app.workato.com/browse/recipes?q=app:yarooms
        name: Yarooms
      - aid: yext
        url: https://app.workato.com/browse/recipes?q=app:yext
        name: Yext
      - aid: youcanbookme
        url: https://app.workato.com/browse/recipes?q=app:youcanbookme
        name: YouCanBookMe
      - aid: youtube
        url: https://app.workato.com/browse/recipes?q=app:youtube
        name: Youtube
      - aid: zendesk-sell
        url: https://app.workato.com/browse/recipes?q=app:zendesk-sell
        name: Zendesk Sell
      - aid: zep
        url: https://app.workato.com/browse/recipes?q=app:zep
        name: ZEP
      - aid: zerobounce
        url: https://app.workato.com/browse/recipes?q=app:zerobounce
        name: ZeroBounce
      - aid: zoho-calendar
        url: https://app.workato.com/browse/recipes?q=app:zoho-calendar
        name: Zoho Calendar
      - aid: zoho-desk
        url: https://app.workato.com/browse/recipes?q=app:zoho-desk
        name: Zoho Desk
      - aid: zoho-mail
        url: https://app.workato.com/browse/recipes?q=app:zoho-mail
        name: Zoho Mail
      - aid: zoho-zeptomail
        url: https://app.workato.com/browse/recipes?q=app:zoho-zeptomail
        name: Zoho ZeptoMail
      - aid: zoom-contact-center
        url: https://app.workato.com/browse/recipes?q=app:zoom-contact-center
        name: Zoom Contact Center
      - aid: zoom-phone
        url: https://app.workato.com/browse/recipes?q=app:zoom-phone
        name: Zoom Phone
      - aid: zoom-team-chat
        url: https://app.workato.com/browse/recipes?q=app:zoom-team-chat
        name: Zoom Team Chat
      - aid: zscaler-client-connector
        url: https://app.workato.com/browse/recipes?q=app:zscaler-client-connector
        name: Zscaler Client Connector
    name: Workato Community Recipes | Workato
    type: Integrations
    description: 'null'
  - url: https://docs.workato.com/en/
    name: Workato Docs
    type: Documentation
    description: 'null'
  - url: https://app.workato.com/browse/recipes
    name: Workato Community Recipes | Workato
    type: Integrations
    description: 'null'
  - data:
      - name: Salesforce
        url: https://www.workato.com/integrations/salesforce
        features:
          - Salesforce
          - CRM
          - Lead Management
          - Order-To-Cash
          - Sales Automation
          - Data Synchronization
          - Workflow Automation
      - name: Slack
        url: https://www.workato.com/integrations/slack
        features:
          - Slack
          - Team Messaging
          - Approval Workflows
          - ChatOps
          - Notifications
          - Workbot
          - Collaboration
      - name: Marketo
        url: https://www.workato.com/integrations/marketo
        features:
          - Marketo
          - Marketing Automation
          - Lead Management
          - Lead Scoring
          - Campaign Management
          - Sales Alignment
          - Demand Generation
      - name: NetSuite REST
        url: https://www.workato.com/integrations/netsuite_rest
        features:
          - NetSuite
          - ERP
          - Financial Management
          - Record Management
          - SuiteQL
          - Order Management
          - Enterprise Resource Planning
      - name: Google Drive
        url: https://www.workato.com/integrations/google_drive
        features:
          - Google Drive
          - Cloud Storage
          - File Management
          - Document Automation
          - Sales Enablement
          - Folder Monitoring
          - Google Workspace
      - name: Workday
        url: https://www.workato.com/integrations/workday
        features:
          - Workday
          - HRIS
          - Employee Onboarding
          - Offboarding
          - Recruiting Automation
          - HR Workflows
          - Payroll
      - name: ServiceNow
        url: https://www.workato.com/integrations/service_now
        features:
          - ServiceNow
          - ITSM
          - Incident Management
          - IT Operations
          - Help Desk
          - Employee Onboarding
          - Ticket Routing
      - name: Snowflake
        url: https://www.workato.com/integrations/snowflake
        features:
          - Snowflake
          - Data Warehouse
          - Data Synchronization
          - SQL Queries
          - Data Consolidation
          - Analytics
          - Cloud Database
      - name: Zendesk
        url: https://www.workato.com/integrations/zendesk
        features:
          - Zendesk
          - Customer Support
          - Ticket Management
          - Help Desk
          - Cross-System Routing
          - Notifications
          - CRM Integration
      - name: Jira
        url: https://www.workato.com/integrations/jira
        features:
          - Jira
          - Project Management
          - DevOps Automation
          - Issue Tracking
          - Support Escalation
          - Agile Workflows
          - ChatOps
      - name: OpenAI
        url: https://www.workato.com/integrations/open_ai
        features:
          - OpenAI
          - Artificial Intelligence
          - Text Analysis
          - Content Generation
          - Image Processing
          - Language Translation
          - AI Automation
      - name: DeepSeek
        url: https://www.workato.com/integrations/deepseek
        features:
          - DeepSeek
          - Artificial Intelligence
          - Chat Completion
          - Large Language Model
          - AI Automation
          - Model Integration
          - Generative AI
      - name: Google Gemini
        url: https://www.workato.com/integrations/google-gemini
        features:
          - Google Gemini
          - Artificial Intelligence
          - Text Analysis
          - Content Generation
          - Image Analysis
          - Language Translation
          - Google AI
      - name: AWS Bedrock
        url: https://www.workato.com/integrations/aws-bedrock
        features:
          - AWS Bedrock
          - Amazon Web Services
          - Foundation Models
          - Text Generation
          - Image Generation
          - AI Automation
          - Cloud AI
      - name: Azure OpenAI
        url: https://www.workato.com/integrations/azure_open_ai
        features:
          - Azure OpenAI
          - Microsoft Azure
          - Artificial Intelligence
          - Text Analysis
          - Content Generation
          - Language Translation
          - Enterprise AI
      - name: Amazon S3
        url: https://www.workato.com/integrations/amazon_s3
        features:
          - Amazon S3
          - Cloud Storage
          - File Management
          - Data Consolidation
          - AWS
          - Object Storage
          - Data Pipeline
      - name: Amazon Redshift
        url: https://www.workato.com/integrations/redshift
        features:
          - Amazon Redshift
          - Data Warehouse
          - Cloud Analytics
          - Data Centralization
          - SQL
          - AWS
          - Business Intelligence
      - name: Azure Blob Storage
        url: https://www.workato.com/integrations/azure_blob_storage
        features:
          - Azure Blob Storage
          - Microsoft Azure
          - Cloud Storage
          - File Management
          - Blob Management
          - Event Triggers
          - Data Pipeline
      - name: MongoDB Atlas
        url: https://www.workato.com/integrations/mongodb
        features:
          - MongoDB
          - NoSQL Database
          - Document Management
          - Data Synchronization
          - Cloud Database
          - Atlas
          - Data Replication
      - name: PostgreSQL
        url: https://www.workato.com/integrations/postgresql
        features:
          - PostgreSQL
          - Relational Database
          - Data Migration
          - SQL Queries
          - Data Pipeline
          - Backup Automation
          - Data Warehouse Integration
      - name: Microsoft SQL Server
        url: https://www.workato.com/integrations/microsoftsqlserver
        features:
          - Microsoft SQL Server
          - Relational Database
          - SQL
          - Data Integration
          - Enterprise Database
          - Workflow Automation
          - Data Synchronization
    name: Integrations
    type: Integrations
  - url: https://www.workato.com/legal
    name: "Workato \x14 Connect your apps. Automate your work. | Workato"
    type: PrivacyPolicy
    description: 'null'
  - url: https://www.workato.com/legal/terms-of-service
    name: "Workato \x14 Connect your apps. Automate your work. | Workato"
    type: TermsOfService
    description: 'null'
  - url: https://www.workato.com/legal/security
    name: "Workato \x14 Connect your apps. Automate your work. | Workato"
    type: Security
    description: 'null'
  - url: https://www.workato.com/about_us
    name: About Us | Workato
    type: About
    description: 'null'
  - url: https://www.workato.com/
    name: 'The #1 iPaaS for the AI and Agentic Era | Workato'
    type: Website
    description: 'null'
  - url: https://app.workato.com/users/sign_in?_gl=1*191kgyn*_gcl_au*MjA2NDIyNDEyNS4xNzQ5MTM5OTgw
    name: Login to build your integrations, automations | Workato
    type: Login
    description: 'null'
  - url: https://docs.workato.com/en/workato-api.html#http-response-codes
    name: Workato API - Introduction | Workato Docs
    type: Errors
    description: 'null'
  - url: https://docs.workato.com/en/mcp.html
    name: MCP | Workato Docs
    type: MCP
    description: 'null'
  - data:
      - Base Workspace from ~$10K/year
      - 'Typical mid-market: $15K-$50K/year'
      - Cost based on recipes + tasks + connectors + user seats
      - High-Volume Recipes (HVR) flat-rate option
      - 'Enterprise: on-prem agent, dedicated support'
      - 1,200+ pre-built connectors
      - Recipes (workflows) and Tasks (actions)
      - Workbot for chat-driven automation
      - Embedded iPaaS for SaaS vendors
      - AI Copilot for recipe generation
      - RecipeIQ for performance tuning
      - 'Recipe API trigger: 6,000 req/min/recipe'
      - 'Concurrent runtime: 100 per workspace'
      - Connector SDK for custom integrations
      - SOC 2 Type 2 + HIPAA + GDPR compliant
      - On-prem agent for behind-the-firewall systems
    name: Features
    type: Features
    sources:
      - https://www.workato.com/pricing
    updated: '2026-05-04'
  - url: https://docs.workato.com/
    type: Developer Portal
  - url: https://docs.workato.com/workato-api/authentication.html
    type: Authentication
  - url: https://docs.workato.com/workato-api/rate-limiting.html
    type: Rate Limits
  - url: https://status.workato.com/
    type: Status Page
  - url: https://community.workato.com/
    type: Community
  - url: https://support.workato.com/
    type: Support
  - url: https://www.workato.com/users/sign_up
    type: Sign Up
  - url: https://www.linkedin.com/company/workato/
    name: Workato on LinkedIn
    type: LinkedIn
  - url: https://twitter.com/workato
    name: Workato on X (Twitter)
    type: Twitter
  - url: https://www.youtube.com/user/workato
    name: Workato on YouTube
    type: YouTube
  - url: https://www.facebook.com/workato/
    name: Workato on Facebook
    type: Facebook
  - url: https://www.instagram.com/workatohq/
    name: Workato on Instagram
    type: Instagram
  - url: https://academy.workato.com/
    name: Workato Academy
    type: Academy
  - url: https://www.workato.com/certification
    name: Workato Certification
    type: Certification
  - url: https://systematic.workato.com/
    name: Workato Systematic Community
    type: Forum
  - url: https://www.workato.com/events
    name: Workato Events
    type: Events
  - url: https://trust.workato.com/
    name: Workato Trust Center
    type: TrustCenter
  - url: https://www.workato.com/press
    name: Workato Press
    type: Press
  - url: https://www.workato.com/careers
    name: Workato Careers
    type: Careers
  - url: https://www.workato.com/request_demo
    name: Contact Sales | Workato
    type: Contact
  - url: https://www.workato.com/embed-saas-integrations
    name: Embedded iPaaS | Workato
    type: Product
  - url: https://docs.workato.com/on-prem.html
    name: On-Prem Connectivity | Workato Docs
    type: Documentation
  - url: https://docs.workato.com/developing-connectors/sdk.html
    name: Connector SDK Developer Program | Workato Docs
    type: SDK
  - url: https://docs.workato.com/api-management.html
    name: API Platform | Workato Docs
    type: Documentation
  - url: https://docs.workato.com/api-mgmt/api-developer-portal.html
    name: API Portal | Workato Docs
    type: Portal
  - url: https://partners.workato.com/
    name: Workato Partner Directory
    type: Partners
  - url: https://www.workato.com/events/automate
    name: Workato Automate Conference
    type: Events
  - url: json-ld/workato-context.jsonld
    type: JSON-LD
  - url: json-schema/workato-recipe-schema.json
    type: JSONSchema
  - url: json-schema/workato-genie-schema.json
    type: JSONSchema
  - url: json-schema/workato-developer-api-recipe-schema.json
    type: JSONSchema
  - url: json-schema/workato-developer-api-data-table-schema.json
    type: JSONSchema
  - url: json-schema/workato-agent-studio-genie-schema.json
    type: JSONSchema
  - url: json-schema/workato-agent-studio-skill-schema.json
    type: JSONSchema
  - url: json-schema/workato-agent-studio-knowledge-base-schema.json
    type: JSONSchema
  - url: json-schema/workato-event-streams-message-schema.json
    type: JSONSchema
  - url: json-schema/workato-mcp-server-mcp-server-schema.json
    type: JSONSchema
  - url: json-schema/workato-mcp-server-tool-schema.json
    type: JSONSchema
  - url: rules/workato-spectral-rules.yml
    type: SpectralRules
  - url: capabilities/automation-management.yaml
    type: NaftikoCapability
    title: Automation Management
  - url: capabilities/shared/developer-api.yaml
    type: NaftikoCapability
    title: Developer API (Shared)
  - url: capabilities/shared/agent-studio.yaml
    type: NaftikoCapability
    title: Agent Studio (Shared)
  - url: capabilities/shared/mcp-server.yaml
    type: NaftikoCapability
    title: MCP Server (Shared)
  - url: capabilities/shared/event-streams.yaml
    type: NaftikoCapability
    title: Event Streams (Shared)
  - url: vocabulary/workato-vocabulary.yml
    type: Vocabulary
created: '2025-06-05T00:00:00.000Z'
modified: '2026-05-04'
position: Consumer
segments:
  - iPaaS
  - Embedded_iPaaS
  - Workflows
description: Workato is an enterprise automation and integration platform that enables organizations to integrate their apps and automate business workflows without extensive coding. It provides a low-code/no-code interface for creating integrations between cloud applications, on-premises systems, and databases.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
