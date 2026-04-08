---
aid: peoplesoft
url: https://raw.githubusercontent.com/api-evangelist/peoplesoft/refs/heads/main/apis.yml
apis:
- name: PeopleSoft REST API
  description: RESTful web services for PeopleSoft applications enabling integration with external systems via the PeopleTools platform.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/en/applications/peoplesoft/
  baseURL: https://{hostname}:{port}/psft/api/v1
  tags:
  - Integration
  - REST
  - Web Services
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/E92519_02/pt856pbr3/eng/pt/tpcl/index.html
  - type: Authentication
    url: https://docs.oracle.com/cd/F30998_01/pt858pbr2/eng/pt/tsec/concept_UnderstandingOAuth2_0.html
  - type: OpenAPI
    url: openapi/rest-api.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Application Services Framework API
  description: Modern REST API layer introduced in PeopleTools 8.59 that produces fully compliant OpenAPI/Swagger specifications, supports proper HTTP status codes, uniform URLs, and JSON payloads for integration with Oracle Integration Cloud, mobile apps, and microservices.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/cd/E52319_01/infoportal/asf.html
  baseURL: https://{hostname}:{port}/psft/asf/v1
  tags:
  - Integration
  - Modern
  - OpenAPI
  - REST
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/E52319_01/infoportal/asf.html
  - type: OpenAPI
    url: openapi/application-services-framework.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Integration Broker
  description: Message-based integration framework for synchronous and asynchronous communication supporting both SOAP and REST protocols.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/cd/E92519_02/pt856pbr3/eng/pt/tibr/index.html
  baseURL: https://{hostname}:{port}/PSIGW/RESTListeningConnector
  tags:
  - Integration
  - Messaging
  - REST
  - SOAP
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/applications/peoplesoft/integration-broker/
  - type: OpenAPI
    url: openapi/integration-broker.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Query API
  description: Execute PeopleSoft Query definitions and retrieve results via REST including the Query Access Service operations for listing, executing, and managing queries.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/en/applications/peoplesoft/query-api/
  baseURL: https://{hostname}:{port}/psft/api/query/v1
  tags:
  - Data Access
  - QAS
  - Query
  - Reporting
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/E92519_02/pt856pbr3/eng/pt/trws/concept_QueryAccessServiceOperations-1f7e36.html
  - type: OpenAPI
    url: openapi/query.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Component Interface API
  description: Programmatic access to PeopleSoft components for data manipulation providing CRUD operations on component data via REST.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/en/applications/peoplesoft/component-interfaces/
  baseURL: https://{hostname}:{port}/psft/api/componentinterface/v1
  tags:
  - Component Interface
  - CRUD Operations
  - Data Access
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/E92519_02/pt856pbr3/eng/pt/tcpi/index.html
  - type: OpenAPI
    url: openapi/component-interface.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Search Framework API
  description: Search indexing and query capabilities powered by OpenSearch (previously Elasticsearch) for full-text search, analytics dashboards, and PeopleSoft Insights.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/cd/E52319_01/infoportal/search.html
  baseURL: https://{hostname}:{port}/psft/api/search/v1
  tags:
  - Analytics
  - Insights
  - OpenSearch
  - Search
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/E52319_01/infoportal/search.html
  - type: OpenAPI
    url: openapi/search-framework.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Data Distribution Framework API
  description: Framework for extracting and flattening PeopleSoft data for machine learning and analytics purposes. Uses PeopleSoft Search Framework technology with OpenSearch to build, index, and register data models that can be exposed as REST APIs.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/cd/F44200_01/pt859pbr2/eng/pt/tmlf/concept_UnderstandingDataDistributionFramework.html
  baseURL: https://{hostname}:{port}/psft/api/ddf/v1
  tags:
  - Analytics
  - Data Distribution
  - Data Extraction
  - Machine Learning
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/F44200_01/pt859pbr2/eng/pt/tmlf/concept_UnderstandingDataDistributionFramework.html
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Notification Framework API
  description: Push notification and event-driven notification services including the Notification Composer for email, text, and in-app notifications. Requires PeopleTools 8.59.19+.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/cd/E41507_01/epm91pbr3/eng/epm/eewe/concept_PeopleSoftEventsandNotificationsFrameworkOverview-227ff2.html
  baseURL: https://{hostname}:{port}/psft/api/notifications/v1
  tags:
  - Events
  - Messaging
  - Notifications
  - Push Notifications
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/E41507_01/epm91pbr3/eng/epm/eewe/concept_PeopleSoftEventsandNotificationsFrameworkOverview-227ff2.html
  - type: OpenAPI
    url: openapi/notification-framework.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Chatbot Integration Framework API
  description: Integration framework for connecting PeopleSoft with Oracle Digital Assistant (ODA) including REST services for chatbot data retrieval and embedded chatbot UI on Fluid pages (PICASO). Requires PeopleTools 8.57.07+.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/cd/E52319_01/infoportal/chatbot.html
  baseURL: https://{hostname}:{port}/psft/api/chatbot/v1
  tags:
  - Chatbot
  - Conversational AI
  - Digital Assistant
  - PICASO
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/E52319_01/infoportal/chatbot.html
  - type: FAQ
    url: https://docs.oracle.com/cd/E52319_01/infoportal/peoplesoft_chatbot_faq.html
  - type: OpenAPI
    url: openapi/chatbot-integration.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Approval Workflow Engine API
  description: Framework for creating, running, and managing approval processes exposable via REST service operations through Integration Broker or ASF.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/en/applications/peoplesoft/
  baseURL: https://{hostname}:{port}/psft/api/approvals/v1
  tags:
  - Approvals
  - AWE
  - Workflow
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/applications/peoplesoft/
  - type: OpenAPI
    url: openapi/approval-workflow-engine.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Process Scheduler API
  description: Process request APIs for submitting and scheduling batch jobs, monitoring process run status, viewing logs, and Application Engine batch processing statistics.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/cd/E24150_01/pt851h2/eng/psbooks/tprs/htm/tprs05.htm
  baseURL: https://{hostname}:{port}/psft/api/scheduler/v1
  tags:
  - Batch Processing
  - Process Monitor
  - Scheduling
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/E24150_01/pt851h2/eng/psbooks/tprs/htm/tprs05.htm
  - type: OpenAPI
    url: openapi/process-scheduler.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Cloud Manager API
  description: REST APIs for automated environment provisioning and deployment on Oracle Cloud Infrastructure including PeopleTools upgrades, update management, and self-service provisioning templates.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/cd/E52319_01/infoportal/cloudmgr.html
  baseURL: https://{hostname}:{port}/psft/api/cloudmgr/v1
  tags:
  - Cloud
  - Deployment
  - OCI
  - Provisioning
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/E52319_01/infoportal/cloudmgr.html
  - type: OpenAPI
    url: openapi/cloud-manager.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Update Manager API
  description: REST services for automated update image management, change package generation, and PeopleSoft Automated Updates (PAU).
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/cd/E52319_01/infoportal/pum.html
  baseURL: https://{hostname}:{port}/psft/api/pum/v1
  tags:
  - Lifecycle Management
  - Patching
  - Updates
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/E52319_01/infoportal/pum.html
  - type: OpenAPI
    url: openapi/update-manager.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Pivot Grid API
  description: Operational dashboard reporting using PS Query, Composite Query, or component data sources accessible via web services for analytics and visualization.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/cd/F28299_01/pt857pbr3/eng/pt/tpvg/concept_PeopleSoftPivotGridOverview-1e7c6b.html
  baseURL: https://{hostname}:{port}/psft/api/pivotgrid/v1
  tags:
  - Analytics
  - Dashboards
  - Pivot Grid
  - Reporting
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/F28299_01/pt857pbr3/eng/pt/tpvg/concept_PeopleSoftPivotGridOverview-1e7c6b.html
  - type: OpenAPI
    url: openapi/pivot-grid.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft HCM API
  description: Human Capital Management APIs for employee data, benefits, payroll, workforce administration, and talent management.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/en/applications/peoplesoft/human-capital-management/index.html
  baseURL: https://{hostname}:{port}/psft/api/hcm/v1
  tags:
  - Benefits
  - HCM
  - HR
  - Payroll
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/applications/peoplesoft/human-capital-management/index.html
  - type: Reference
    url: https://docs.oracle.com/cd/F58024_01/hcm92pbr43/eng/hcm/ecch/UnderstandingRestApiEndpointsForPeoplesoftSkills.html
  - type: OpenAPI
    url: openapi/hcm.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Employee Directory API
  description: REST API for retrieving employee details by name or employee ID, and for looking up direct reports based on manager name or ID. Supports the Employee Directory chatbot skill and integration with external directories.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/cd/G20540_01/hcm92pbr51/eng/hcm/ecch/UnderstandingRESTAPIEndpointsForPeoplesoftEmployeeDirectoryemployeedirectory.html
  baseURL: https://{hostname}:{port}/psft/api/hcm/employeedirectory/v1
  tags:
  - Employee Directory
  - HCM
  - Workforce Data
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/G20540_01/hcm92pbr51/eng/hcm/ecch/UnderstandingRESTAPIEndpointsForPeoplesoftEmployeeDirectoryemployeedirectory.html
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Absence Management API
  description: REST API for creating, updating, and retrieving absence requests, viewing employee absence balances by type, and retrieving absence configuration rules. Supports Absence Management chatbot skill and self-service integrations.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/cd/F70351_01/cs92pbr27/eng/cs/eccs/UnderstandingRESTAPIEndpointsForPeopleSoftAbsenceManagementApplicationServicesabsence.html
  baseURL: https://{hostname}:{port}/psft/api/hcm/absence/v1
  tags:
  - Absence Management
  - HCM
  - Leave
  - Time Off
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/F70351_01/cs92pbr27/eng/cs/eccs/UnderstandingRESTAPIEndpointsForPeopleSoftAbsenceManagementApplicationServicesabsence.html
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Recruiting and Talent Management API
  description: REST endpoints for job search services, Candidate Gateway self-service, recruiting solutions, and talent management workflows.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/cd/F85027_01/hcm92pbr47/eng/hcm/ecch/UnderstandingRESTAPIEndpointsForPeopleSoftJobSearchServiceshrsjobs.html
  baseURL: https://{hostname}:{port}/psft/api/hcm/recruiting/v1
  tags:
  - Candidate Gateway
  - Job Search
  - Recruiting
  - Talent Management
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/F85027_01/hcm92pbr47/eng/hcm/ecch/UnderstandingRESTAPIEndpointsForPeopleSoftJobSearchServiceshrsjobs.html
  - type: OpenAPI
    url: openapi/recruiting-talent-management.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Payroll for North America API
  description: Delivered REST API endpoints for retrieving paycheck header details, earnings, deductions, taxes, direct deposits, employer paid benefits, garnishments, and year-end forms for North American payroll processing.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/cd/F57918_01/ps91pbr14/eng/ps/eccp/UnderstandingRestApiEndpointsForPeoplesoftPayrollForNorthAmericaSkill.html
  baseURL: https://{hostname}:{port}/psft/api/hcm/payrollbankingyearendforms/v1
  tags:
  - Compensation
  - HCM
  - North America
  - Payroll
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/F57918_01/ps91pbr14/eng/ps/eccp/UnderstandingRestApiEndpointsForPeoplesoftPayrollForNorthAmericaSkill.html
  - type: Reference
    url: https://docs.oracle.com/cd/F82673_01/elm92pbr23/eng/elm/eccl/UnderstandingRESTAPIEndpointsForPeoplesoftPayrollForNorthAmericaServicespayrollbankingyearendforms.html
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Global Payroll API
  description: REST API endpoints for the Global Payroll skill, providing access to payroll data, product profile information, and chatbot framework resources for international payroll processing across multiple countries.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/cd/F58738_01/cs92pbr26/eng/cs/eccs/UnderstandingRestApiEndpointsForPeoplesoftGlobalPayrollSkill.html
  baseURL: https://{hostname}:{port}/psft/api/hcm/globalpayroll/v1
  tags:
  - Global Payroll
  - HCM
  - International
  - Payroll
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/F58738_01/cs92pbr26/eng/cs/eccs/UnderstandingRestApiEndpointsForPeoplesoftGlobalPayrollSkill.html
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft HR Common Utility Services API
  description: REST API for retrieving employee country and business partner contact details. Shared utility services used across all delivered HCM skills and integration scenarios.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/cd/F85282_01/cs92pbr30/eng/cs/eccs/UnderstandingRESTAPIEndpointsforPeopleSoftHRCommonUtilityServices.html
  baseURL: https://{hostname}:{port}/psft/api/hcm/hcmcommonutilities/v1
  tags:
  - Employee Data
  - HCM
  - Utilities
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/F85282_01/cs92pbr30/eng/cs/eccs/UnderstandingRESTAPIEndpointsforPeopleSoftHRCommonUtilityServices.html
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Financials API
  description: Financial Management APIs for general ledger, accounts payable, accounts receivable, expenses, asset management, and financial reporting.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/en/applications/peoplesoft/financial-management/index.html
  baseURL: https://{hostname}:{port}/psft/api/financials/v1
  tags:
  - AP
  - AR
  - Expenses
  - Financials
  - General Ledger
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/applications/peoplesoft/financial-management/index.html
  - type: OpenAPI
    url: openapi/financials.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Expenses API
  description: Delivered REST API endpoints for expense report management including fetching expense reports by status, creation date, or sheet name, retrieving transaction details, managing wallet entries, expense type validation, and notification services for travel and expense processing.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/cd/F48195_01/cs92pbr23/eng/cs/eccs/UnderstandingRestApiEndpointsForPeoplesoftExpenseSkill.html
  baseURL: https://{hostname}:{port}/psft/api/fscm/expenses/v1
  tags:
  - Expense Reports
  - Expenses
  - Financials
  - Travel
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/F48195_01/cs92pbr23/eng/cs/eccs/UnderstandingRestApiEndpointsForPeoplesoftExpenseSkill.html
  - type: Reference
    url: https://docs.oracle.com/cd/G47724_01/fscm92pbr55/eng/fscm/eccf/UnderstandingRESTAPIEndpointsForPeopleSoftGetTransactionDetailsexgettransdetails.html
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft eSettlements API
  description: Delivered REST API endpoints for invoice and payment management including fetching disputed invoices, invoice status inquiries, payment status tracking, payment inquiries, and payment difference resolution for supplier settlement processing.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/cd/F57918_01/ps91pbr14/eng/ps/eccp/UnderstandingRESTAPIEndpointsforPeopleSofteSettlementsSkill.html
  baseURL: https://{hostname}:{port}/psft/api/fscm/esettlements/v1
  tags:
  - eSettlements
  - Financials
  - Invoices
  - Payments
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/F57918_01/ps91pbr14/eng/ps/eccp/UnderstandingRESTAPIEndpointsforPeopleSofteSettlementsSkill.html
  - type: Reference
    url: https://docs.oracle.com/cd/G35227_01/fscm92pbr54/eng/fscm/eccf/UnderstandingRESTAPIEndpointsForPeopleSoftFetchPaymentStatusespaymentstatus.html
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Supply Chain Management API
  description: REST API endpoints for procurement, inventory management, order fulfillment, logistics, and enterprise integration points for warehouse management systems.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/cd/F92336_01/fscm92pbr50/eng/fscm/eccf/UnderstandingRestApiEndpointsForPeoplesoft.html
  baseURL: https://{hostname}:{port}/psft/api/scm/v1
  tags:
  - Inventory
  - Logistics
  - Order Fulfillment
  - Procurement
  - Supply Chain
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/F92336_01/fscm92pbr50/eng/fscm/eccf/UnderstandingRestApiEndpointsForPeoplesoft.html
  - type: OpenAPI
    url: openapi/supply-chain-management.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft eProcurement API
  description: Delivered REST API endpoints for requisition management including retrieving requisitions for items, getting requester lists and names, and checking requisition status. Supports the full procure-to-pay lifecycle from requisition creation through purchase order dispatch and receiving.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/cd/F92336_01/fscm92pbr50/eng/fscm/eccf/UnderstandingRestApiEndpointsForPeoplesoft.html
  baseURL: https://{hostname}:{port}/psft/api/fscm/eprocurement/v1
  tags:
  - eProcurement
  - Purchasing
  - Requisitions
  - Supply Chain
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/F92336_01/fscm92pbr50/eng/fscm/eccf/UnderstandingRestApiEndpointsForPeoplesoft.html
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Supplier Portal API
  description: Comprehensive REST API for the Supplier Portal providing access to bid details, managed content such as announcements and events, overdue shipment tracking, purchase order acknowledgement, invoice and payment inquiries, and sourcing operations across secure and public supplier collaboration channels.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/cd/G20540_01/hcm92pbr51/eng/hcm/ecch/UnderstandingRESTAPIEndpointsForPeopleSoftSupplierComprehensivePortalServicescp.html
  baseURL: https://{hostname}:{port}/psft/api/fscm/scp/v1
  tags:
  - Sourcing
  - Supplier Collaboration
  - Supplier Portal
  - Supply Chain
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/G20540_01/hcm92pbr51/eng/hcm/ecch/UnderstandingRESTAPIEndpointsForPeopleSoftSupplierComprehensivePortalServicescp.html
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft CRM API
  description: Customer Relationship Management REST API endpoints and integration points for customer data, case management, sales, and marketing.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/cd/F95753_01/crm92pbr22/eng/crm/eccc/UnderstandingRestApiEndpointsForPeoplesoft.html
  baseURL: https://{hostname}:{port}/psft/api/crm/v1
  tags:
  - Case Management
  - CRM
  - Customer Data
  - Marketing
  - Sales
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/F95753_01/crm92pbr22/eng/crm/eccc/UnderstandingRestApiEndpointsForPeoplesoft.html
  - type: OpenAPI
    url: openapi/crm.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Campus Solutions API
  description: Campus Solutions APIs for student records, admissions, enrollment, financial aid, and academic advising.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/en/applications/peoplesoft/campus-solutions/index.html
  baseURL: https://{hostname}:{port}/psft/api/campus/v1
  tags:
  - Admissions
  - Campus Solutions
  - Education
  - Financial Aid
  - Student Records
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/applications/peoplesoft/campus-solutions/index.html
  - type: OpenAPI
    url: openapi/campus-solutions.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Enterprise Performance Management API
  description: Analytics, budgeting, forecasting, and planning APIs with events and notifications framework for financial and operational performance management.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/cd/E41507_01/epm91pbr3/eng/epm/penw/index.html
  baseURL: https://{hostname}:{port}/psft/api/epm/v1
  tags:
  - Analytics
  - Budgeting
  - EPM
  - Forecasting
  - Planning
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/E41507_01/epm91pbr3/eng/epm/penw/index.html
  - type: OpenAPI
    url: openapi/enterprise-performance-management.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Interaction Hub API
  description: Content management, branding, and portal administration APIs for the PeopleSoft Interaction Hub (formerly Enterprise Portal) with Integration Broker services.
  image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
  humanURL: https://docs.oracle.com/cd/F75142_01/ps91pbr15/eng/ps/psad/PeopleSoftInteractionHubOverview.html
  baseURL: https://{hostname}:{port}/psft/api/hub/v1
  tags:
  - Branding
  - Content Management
  - Interaction Hub
  - Portal
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/F75142_01/ps91pbr15/eng/ps/psad/PeopleSoftInteractionHubOverview.html
  - type: OpenAPI
    url: openapi/interaction-hub.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
name: PeopleSoft
tags:
- Campus Solutions
- CRM
- Enterprise Software
- ERP
- Financial Management
- HCM
- Supply Chain Management
type: Contract
image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Collection of Oracle PeopleSoft Enterprise application APIs for Human Capital Management, Financial Management, Supply Chain Management, CRM, Campus Solutions, and engineering intelligence across PeopleTools platform services.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

