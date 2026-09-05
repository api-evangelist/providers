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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 31.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 63
  human_in_the_loop: 0
  name: Eloqua Agentic Access
  operation_count: 111
  slug: eloqua-agentic-access
  summary_line: 111 operations · 63 acting
api_count: 3
apis:
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Export account data in bulk
  name: Oracle Eloqua Account Exports API
  slug: eloqua-account-exports-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Retrieve available account fields for mapping
  name: Oracle Eloqua Account Fields API
  slug: eloqua-account-fields-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Import account data in bulk
  name: Oracle Eloqua Account Imports API
  slug: eloqua-account-imports-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Manage account records and groups
  name: Oracle Eloqua Accounts API
  slug: eloqua-accounts-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Export activity data in bulk
  name: Oracle Eloqua Activity Exports API
  slug: eloqua-activity-exports-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Import activity data in bulk
  name: Oracle Eloqua Activity Imports API
  slug: eloqua-activity-imports-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Create and manage marketing campaigns
  name: Oracle Eloqua Campaigns API
  slug: eloqua-campaigns-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Export contact data in bulk
  name: Oracle Eloqua Contact Exports API
  slug: eloqua-contact-exports-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Retrieve available contact fields for mapping
  name: Oracle Eloqua Contact Fields API
  slug: eloqua-contact-fields-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Import contact data in bulk
  name: Oracle Eloqua Contact Imports API
  slug: eloqua-contact-imports-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Create and manage contact lists
  name: Oracle Eloqua Contact Lists API
  slug: eloqua-contact-lists-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Create and manage contact segments
  name: Oracle Eloqua Contact Segments API
  slug: eloqua-contact-segments-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Manage contact records and data
  name: Oracle Eloqua Contacts API
  slug: eloqua-contacts-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Export custom object data in bulk
  name: Oracle Eloqua Custom Object Exports API
  slug: eloqua-custom-object-exports-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Import custom object data in bulk
  name: Oracle Eloqua Custom Object Imports API
  slug: eloqua-custom-object-imports-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Manage custom object definitions and data
  name: Oracle Eloqua Custom Objects API
  slug: eloqua-custom-objects-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Create and manage email assets
  name: Oracle Eloqua Emails API
  slug: eloqua-emails-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Create and manage forms and form data
  name: Oracle Eloqua Forms API
  slug: eloqua-forms-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Create and manage landing pages
  name: Oracle Eloqua Landing Pages API
  slug: eloqua-landing-pages-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Create and manage automation programs
  name: Oracle Eloqua Programs API
  slug: eloqua-programs-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Manage data synchronization operations
  name: Oracle Eloqua Syncs API
  slug: eloqua-syncs-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Manage system users
  name: Oracle Eloqua Users API
  slug: eloqua-users-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: An Oracle Eloqua Account provides group contact information. <a href='https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/index.html#CSHID=Accounts'>Learn more about accounts</a>.
  name: Oracle Eloqua Application/1.0/Accounts API
  slug: eloqua-application-1-0-accounts-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Activities are tracked for individual contacts.
  name: Oracle Eloqua Application/1.0/Activities API
  slug: eloqua-application-1-0-activities-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Contact fields are the fields associated with a specific contact asset. <a href='https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/index.html#CSHID=ContactFields'>Learn more about contact fiel
  name: Oracle Eloqua Application/1.0/Contact fields API
  slug: eloqua-application-1-0-contact-fields-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Customized lists of contacts.
  name: Oracle Eloqua Application/1.0/Contact list API
  slug: eloqua-application-1-0-contact-list-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Segments API endpoints. <a href='https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/index.html#CSHID=Segments'>Learn more about segments</a>.
  name: Oracle Eloqua Application/1.0/Contact segments API
  slug: eloqua-application-1-0-contact-segments-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: A contact is a data entity that contains the explicit data around an individual person in the database. <a href='https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/index.html#CSHID=Contacts'>Le
  name: Oracle Eloqua Application/1.0/Contacts API
  slug: eloqua-application-1-0-contacts-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Content sections allow you to create shared content to use inside assets such as emails and landing pages. <a href='https://docs.oracle.com/en/cloud/saas/marketing/eloqua-user/index.html#CSHID=SharedC
  name: Oracle Eloqua Application/1.0/Content sections API
  slug: eloqua-application-1-0-content-sections-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Custom object data are the records of custom object instances. <a href='https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/index.html#CSHID=CustomObjects'>Learn more about custom objects</a>.
  name: Oracle Eloqua Application/1.0/Custom object data API
  slug: eloqua-application-1-0-custom-object-data-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: 'Custom objects are a complement to the standard Data Entities (i.e. Contacts, Companies). Essentially, custom objects are used for two main functions: linking directly to a Contact and performing acti'
  name: Oracle Eloqua Application/1.0/Custom objects API
  slug: eloqua-application-1-0-custom-objects-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Email folders organize your email assets. <a href='https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/index.html#CSHID=Emails'>Learn more about emails</a>.
  name: Oracle Eloqua Application/1.0/Email folders API
  slug: eloqua-application-1-0-email-folders-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Email footers are used to customize the look and feel of the bottom of your email. <a href='https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/index.html#CSHID=EmailFooters'>Learn more about em
  name: Oracle Eloqua Application/1.0/Email footers API
  slug: eloqua-application-1-0-email-footers-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Email Groups are used to control default settings for similar types of emails. For instance, you can set the default header, footer, subscription landing page, and unsubscribe landing page for a set o
  name: Oracle Eloqua Application/1.0/Email groups API
  slug: eloqua-application-1-0-email-groups-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Email headers are used to customize the look and feel of the top of your email. Headers can be used in your emails for branding purposes (your company's logo), to provide links to other (external) res
  name: Oracle Eloqua Application/1.0/Email headers API
  slug: eloqua-application-1-0-email-headers-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Despite vast innovations and improvements to other channels of communication with prospects, emails are still central to many marketing campaigns. You can reach a large number of existing and potentia
  name: Oracle Eloqua Application/1.0/Emails API
  slug: eloqua-application-1-0-emails-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Form data are the submissions for a form. <a href='https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/index.html#CSHID=Forms'>Learn more about forms</a>.
  name: Oracle Eloqua Application/1.0/Form data API
  slug: eloqua-application-1-0-form-data-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Form data are the submissions for a form. <a href='https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/index.html#CSHID=Forms'>Learn more about Forms</a>.
  name: Oracle Eloqua Application/1.0/Forms API
  slug: eloqua-application-1-0-forms-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Image assets to be used in places such as emails or landing pages. <a href='https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/index.html#CSHID=Images'>Learn more about images</a>.
  name: Oracle Eloqua Application/1.0/Images API
  slug: eloqua-application-1-0-images-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Landing pages are often the first significant part of a campaign that a contact will see. A contact may be directed to your landing page from a link in an email or from an ad on the web. The landing p
  name: Oracle Eloqua Application/1.0/Landing pages API
  slug: eloqua-application-1-0-landing-pages-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: 'A microsite is a miniature website, often dedicated to a specific campaign, product, or keyword. The purpose is to give a visitor (whether channeled through your website, social media assets, emails, '
  name: Oracle Eloqua Application/1.0/Microsites API
  slug: eloqua-application-1-0-microsites-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Option lists are usually referred to on the marketers' side as select lists or pick lists. <a href='https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/index.html#CSHID=PickLists'>Learn more abo
  name: Oracle Eloqua Application/1.0/Option lists API
  slug: eloqua-application-1-0-option-lists-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Users API endpoints. The API allows you to modify such things as a user's time preference. <a href='https://docs.oracle.com/en/cloud/saas/marketing/eloqua-user/Help/UserManagement/UserManagement.htm'>
  name: Oracle Eloqua Application/1.0/Users API
  slug: eloqua-application-1-0-users-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: An Oracle Eloqua Account Group provides the ability to group multiple companies into an Account Group. <a href='https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/index.html#CSHID=Accounts'>Lea
  name: Oracle Eloqua Application/2.0/Account groups API
  slug: eloqua-application-2-0-account-groups-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: An Oracle Eloqua Account provides group contact information. <a href='https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/index.html#CSHID=Accounts'>Learn more about accounts</a>.
  name: Oracle Eloqua Application/2.0/Accounts API
  slug: eloqua-application-2-0-accounts-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Activities API endpoint.
  name: Oracle Eloqua Application/2.0/Activities API
  slug: eloqua-application-2-0-activities-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The Audit Log API endpoint enables initiating a request for <a href='https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/index.html#CSHID=EloquaAuditing'>Eloqua audit log</a> exports using the A
  name: Oracle Eloqua Application/2.0/Audit logs API
  slug: eloqua-application-2-0-audit-logs-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Campaign fields are the fields associated with a specific campaign asset. <a href='https://docs.oracle.com/en/cloud/saas/marketing/eloqua-user/Help/Administration/Tasks/ConfiguringCustomCampaignFields
  name: Oracle Eloqua Application/2.0/Campaign fields API
  slug: eloqua-application-2-0-campaign-fields-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Campaign folders organize your campaign assets.
  name: Oracle Eloqua Application/2.0/Campaign folders API
  slug: eloqua-application-2-0-campaign-folders-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Marketing campaigns are at the center of the Eloqua application, campaigns are comprised of different elements (such as segments, emails, landing pages, etc.) that are used to perform a variety of fun
  name: Oracle Eloqua Application/2.0/Campaigns API
  slug: eloqua-application-2-0-campaigns-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Contact filter folders organize your contact filters.
  name: Oracle Eloqua Application/2.0/Contact filter folders API
  slug: eloqua-application-2-0-contact-filter-folders-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Contact list folders organize your contact lists.
  name: Oracle Eloqua Application/2.0/Contact list folders API
  slug: eloqua-application-2-0-contact-list-folders-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Contact segment folders to organize your segments.
  name: Oracle Eloqua Application/2.0/Contact segment folders API
  slug: eloqua-application-2-0-contact-segment-folders-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Contact segments are groups of contacts generated based on filter criteria and contact lists. <a href='https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/index.html#CSHID=Segments'>Learn more a
  name: Oracle Eloqua Application/2.0/Contact segments API
  slug: eloqua-application-2-0-contact-segments-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: A contact is a data entity that contains the explicit data around an individual person in the database. <a href='https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/index.html#CSHID=Contacts'>Le
  name: Oracle Eloqua Application/2.0/Contacts API
  slug: eloqua-application-2-0-contacts-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Countries API endpoints.
  name: Oracle Eloqua Application/2.0/Countries API
  slug: eloqua-application-2-0-countries-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Custom object data are the records of custom object instances. <a href='https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/index.html#CSHID=CustomObjects'>Learn more about custom objects</a>.
  name: Oracle Eloqua Application/2.0/Custom object data API
  slug: eloqua-application-2-0-custom-object-data-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: 'Custom objects are a complement to the standard Data Entities (i.e. Contacts, Companies). Essentially, custom objects are used for two main functions: linking directly to a Contact and performing acti'
  name: Oracle Eloqua Application/2.0/Custom objects API
  slug: eloqua-application-2-0-custom-objects-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Dedupe Rule endpoints
  name: Oracle Eloqua Application/2.0/Dedupe Rules API
  slug: eloqua-application-2-0-dedupe-rules-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: 'The email deployment API is used to send and retrieve email deployments. There are two methods for creating and sending email deployments: to a single contact, or to a low volume of contacts (up to 10'
  name: Oracle Eloqua Application/2.0/Email deployment API
  slug: eloqua-application-2-0-email-deployment-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Email folders organize your email assets.
  name: Oracle Eloqua Application/2.0/Email folders API
  slug: eloqua-application-2-0-email-folders-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Emails API Endpoints. <a href='https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/index.html#CSHID=Emails'>Learn more about emails</a>. Creating and updating emails with the type <code>Responsi
  name: Oracle Eloqua Application/2.0/Emails API
  slug: eloqua-application-2-0-emails-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The event registration API is used to manage event registrants. <a href='https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/index.html#CSHID=EventManagement'>Learn more about Event Management</
  name: Oracle Eloqua Application/2.0/Event registrants API
  slug: eloqua-application-2-0-event-registrants-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The events API is used to manage events. <a href='https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/index.html#CSHID=EventManagement'>Learn more about Event Management</a>.
  name: Oracle Eloqua Application/2.0/Events API
  slug: eloqua-application-2-0-events-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: External activities are non-Eloqua (that is, offline) activities performed by your contacts or prospects. These assets can be imported for use in Eloqua campaign reporting. External asset types is the
  name: Oracle Eloqua Application/2.0/External activities API
  slug: eloqua-application-2-0-external-activities-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: External activities are non-Eloqua (that is, offline) activities performed by your contacts or prospects. These assets can be imported for use in Eloqua campaign reporting. External asset types is the
  name: Oracle Eloqua Application/2.0/External asset types API
  slug: eloqua-application-2-0-external-asset-types-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: External assets are non-Eloqua (that is, offline) activities performed by your contacts or prospects. These assets can be imported for use in Eloqua campaign reporting. <a href='https://docs.oracle.co
  name: Oracle Eloqua Application/2.0/External assets API
  slug: eloqua-application-2-0-external-assets-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Form data are the submissions for a form. <a href='https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/index.html#CSHID=Forms'>Learn more about Forms</a>.
  name: Oracle Eloqua Application/2.0/Form data API
  slug: eloqua-application-2-0-form-data-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Form folders organize your form assets.
  name: Oracle Eloqua Application/2.0/Form folders API
  slug: eloqua-application-2-0-form-folders-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Forms API endpoints. <a href='https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/index.html#CSHID=Forms'>Learn more about Forms</a>.
  name: Oracle Eloqua Application/2.0/Forms API
  slug: eloqua-application-2-0-forms-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Hyperlink folders organize your hyperlinks.
  name: Oracle Eloqua Application/2.0/Hyperlink folders API
  slug: eloqua-application-2-0-hyperlink-folders-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Image folders organize your image assets.
  name: Oracle Eloqua Application/2.0/Image folders API
  slug: eloqua-application-2-0-image-folders-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Landing Pages API endpoints. <a href='https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/index.html#CSHID=LandingPages'>Learn more about landing pages</a>.
  name: Oracle Eloqua Application/2.0/Landing pages API
  slug: eloqua-application-2-0-landing-pages-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Lookup table endpoints
  name: Oracle Eloqua Application/2.0/Lookup tables API
  slug: eloqua-application-2-0-lookup-tables-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Programs API endpoints. <a href='https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/index.html#CSHID=ProgramCanvas'>Learn more about Programs</a>.
  name: Oracle Eloqua Application/2.0/Programs API
  slug: eloqua-application-2-0-programs-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Security group API endpoints.
  name: Oracle Eloqua Application/2.0/Security groups API
  slug: eloqua-application-2-0-security-groups-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Signature rule mappings API endpoints.
  name: Oracle Eloqua Application/2.0/Signature Rule Mappings API
  slug: eloqua-application-2-0-signature-rule-mappings-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Signature rules API endpoints.
  name: Oracle Eloqua Application/2.0/Signature Rules API
  slug: eloqua-application-2-0-signature-rules-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: SMS API endpoints.
  name: Oracle Eloqua Application/2.0/SMS API
  slug: eloqua-application-2-0-sms-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: SMS sender codes API endpoints.
  name: Oracle Eloqua Application/2.0/SMS codes API
  slug: eloqua-application-2-0-sms-codes-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: SMS folders organize your SMS assets.
  name: Oracle Eloqua Application/2.0/SMS folders API
  slug: eloqua-application-2-0-sms-folders-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: SMS invalid keyword response message API endpoints.
  name: Oracle Eloqua Application/2.0/SMS invalid keyword messages API
  slug: eloqua-application-2-0-sms-invalid-keyword-messages-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: SMS keywords API endpoints.
  name: Oracle Eloqua Application/2.0/SMS keywords API
  slug: eloqua-application-2-0-sms-keywords-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The SMS subscription API is used to manage phone number consent.
  name: Oracle Eloqua Application/2.0/SMS subscription API
  slug: eloqua-application-2-0-sms-subscription-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: Users API endpoints.
  name: Oracle Eloqua Application/2.0/Users API
  slug: eloqua-application-2-0-users-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: A visitor profile field are the fields associated to a website visitor. <a href='https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAA/index.html#CSHID=VisitorProfileFields'>Learn more about Visit
  name: Oracle Eloqua Application/2.0/Visitor profile fields API
  slug: eloqua-application-2-0-visitor-profile-fields-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: A visitor is a data entity that represents a unique cookie. The tracked activity data from that cookie is associated with the Visitor. There can be multiple visitors linked to a single contact.
  name: Oracle Eloqua Application/2.0/Visitors API
  slug: eloqua-application-2-0-visitors-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Bulk/2.0/accounts category.
  name: Oracle Eloqua Bulk/2.0/accounts API
  slug: eloqua-bulk-2-0-accounts-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Bulk/2.0/activities category.
  name: Oracle Eloqua Bulk/2.0/activities API
  slug: eloqua-bulk-2-0-activities-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Bulk/2.0/campaignResponses category.
  name: Oracle Eloqua Bulk/2.0/campaign Responses API
  slug: eloqua-bulk-2-0-campaignresponses-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Bulk/2.0/campaigns category.
  name: Oracle Eloqua Bulk/2.0/campaigns API
  slug: eloqua-bulk-2-0-campaigns-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Bulk/2.0/contacts category.
  name: Oracle Eloqua Bulk/2.0/contacts API
  slug: eloqua-bulk-2-0-contacts-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Bulk/2.0/customObjects category.
  name: Oracle Eloqua Bulk/2.0/custom Objects API
  slug: eloqua-bulk-2-0-customobjects-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Bulk/2.0/emailAddresses category.
  name: Oracle Eloqua Bulk/2.0/email Addresses API
  slug: eloqua-bulk-2-0-emailaddresses-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Bulk/2.0/emailGroups category.
  name: Oracle Eloqua Bulk/2.0/email Groups API
  slug: eloqua-bulk-2-0-emailgroups-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Bulk/2.0/events category.
  name: Oracle Eloqua Bulk/2.0/events API
  slug: eloqua-bulk-2-0-events-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Bulk/2.0/exports category.
  name: Oracle Eloqua Bulk/2.0/exports API
  slug: eloqua-bulk-2-0-exports-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Bulk/2.0/imports category.
  name: Oracle Eloqua Bulk/2.0/imports API
  slug: eloqua-bulk-2-0-imports-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Bulk/2.0/opportunities category.
  name: Oracle Eloqua Bulk/2.0/opportunities API
  slug: eloqua-bulk-2-0-opportunities-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Bulk/2.0/phoneNumbers category.
  name: Oracle Eloqua Bulk/2.0/phone Numbers API
  slug: eloqua-bulk-2-0-phonenumbers-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Bulk/2.0/syncActions category.
  name: Oracle Eloqua Bulk/2.0/sync Actions API
  slug: eloqua-bulk-2-0-syncactions-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Bulk/2.0/syncs category.
  name: Oracle Eloqua Bulk/2.0/syncs API
  slug: eloqua-bulk-2-0-syncs-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/AccountActivity/1.0/Account category.
  name: Oracle Eloqua Reporting/Account Activity/1.0/Account API
  slug: eloqua-reporting-accountactivity-1-0-account-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/AccountActivity/1.0/AccountEngagement category.
  name: Oracle Eloqua Reporting/Account Activity/1.0/Account Engagement API
  slug: eloqua-reporting-accountactivity-1-0-accountengagement-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/ActivityDetails/1.0/Campaign category.
  name: Oracle Eloqua Reporting/Activity Details/1.0/Campaign API
  slug: eloqua-reporting-activitydetails-1-0-campaign-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/ActivityDetails/1.0/CampaignResponse category.
  name: Oracle Eloqua Reporting/Activity Details/1.0/Campaign Response API
  slug: eloqua-reporting-activitydetails-1-0-campaignresponse-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/ActivityDetails/1.0/Contact category.
  name: Oracle Eloqua Reporting/Activity Details/1.0/Contact API
  slug: eloqua-reporting-activitydetails-1-0-contact-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/ActivityDetails/1.0/ContactIntegrationFields category.
  name: Oracle Eloqua Reporting/Activity Details/1.0/Contact Integration Fields API
  slug: eloqua-reporting-activitydetails-1-0-contactintegrationfields-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/ActivityDetails/1.0/Device category.
  name: Oracle Eloqua Reporting/Activity Details/1.0/Device API
  slug: eloqua-reporting-activitydetails-1-0-device-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/ActivityDetails/1.0/EloquaLinkedAccount category.
  name: Oracle Eloqua Reporting/Activity Details/1.0/Eloqua Linked Account API
  slug: eloqua-reporting-activitydetails-1-0-eloqualinkedaccount-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/ActivityDetails/1.0/EmailAsset category.
  name: Oracle Eloqua Reporting/Activity Details/1.0/Email Asset API
  slug: eloqua-reporting-activitydetails-1-0-emailasset-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/ActivityDetails/1.0/EmailAutoClick category.
  name: Oracle Eloqua Reporting/Activity Details/1.0/Email Auto Click API
  slug: eloqua-reporting-activitydetails-1-0-emailautoclick-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/ActivityDetails/1.0/EmailAutoOpen category.
  name: Oracle Eloqua Reporting/Activity Details/1.0/Email Auto Open API
  slug: eloqua-reporting-activitydetails-1-0-emailautoopen-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/ActivityDetails/1.0/EmailBounceback category.
  name: Oracle Eloqua Reporting/Activity Details/1.0/Email Bounceback API
  slug: eloqua-reporting-activitydetails-1-0-emailbounceback-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/ActivityDetails/1.0/EmailClickthrough category.
  name: Oracle Eloqua Reporting/Activity Details/1.0/Email Clickthrough API
  slug: eloqua-reporting-activitydetails-1-0-emailclickthrough-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/ActivityDetails/1.0/EmailGroup category.
  name: Oracle Eloqua Reporting/Activity Details/1.0/Email Group API
  slug: eloqua-reporting-activitydetails-1-0-emailgroup-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/ActivityDetails/1.0/EmailGroupSubscriptionStatus category.
  name: Oracle Eloqua Reporting/Activity Details/1.0/Email Group Subscription Status API
  slug: eloqua-reporting-activitydetails-1-0-emailgroupsubscriptionstatus-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/ActivityDetails/1.0/EmailOpen category.
  name: Oracle Eloqua Reporting/Activity Details/1.0/Email Open API
  slug: eloqua-reporting-activitydetails-1-0-emailopen-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/ActivityDetails/1.0/EmailSend category.
  name: Oracle Eloqua Reporting/Activity Details/1.0/Email Send API
  slug: eloqua-reporting-activitydetails-1-0-emailsend-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/ActivityDetails/1.0/EmailUnsubscribe category.
  name: Oracle Eloqua Reporting/Activity Details/1.0/Email Unsubscribe API
  slug: eloqua-reporting-activitydetails-1-0-emailunsubscribe-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/ActivityDetails/1.0/FormSubmission category.
  name: Oracle Eloqua Reporting/Activity Details/1.0/Form Submission API
  slug: eloqua-reporting-activitydetails-1-0-formsubmission-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/ActivityDetails/1.0/LandingPageVisit category.
  name: Oracle Eloqua Reporting/Activity Details/1.0/Landing Page Visit API
  slug: eloqua-reporting-activitydetails-1-0-landingpagevisit-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/ActivityDetails/1.0/Referrer category.
  name: Oracle Eloqua Reporting/Activity Details/1.0/Referrer API
  slug: eloqua-reporting-activitydetails-1-0-referrer-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/ActivityDetails/1.0/Segment category.
  name: Oracle Eloqua Reporting/Activity Details/1.0/Segment API
  slug: eloqua-reporting-activitydetails-1-0-segment-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/ActivityDetails/1.0/SpamUnsubscribesByEmail category.
  name: Oracle Eloqua Reporting/Activity Details/1.0/Spam Unsubscribes By Email API
  slug: eloqua-reporting-activitydetails-1-0-spamunsubscribesbyemail-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/ActivityDetails/1.0/User category.
  name: Oracle Eloqua Reporting/Activity Details/1.0/User API
  slug: eloqua-reporting-activitydetails-1-0-user-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/CampaignAnalysis/1.0/Calendar category.
  name: Oracle Eloqua Reporting/Campaign Analysis/1.0/Calendar API
  slug: eloqua-reporting-campaignanalysis-1-0-calendar-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/CampaignAnalysis/1.0/Campaign category.
  name: Oracle Eloqua Reporting/Campaign Analysis/1.0/Campaign API
  slug: eloqua-reporting-campaignanalysis-1-0-campaign-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/CampaignAnalysis/1.0/EmailActivities category.
  name: Oracle Eloqua Reporting/Campaign Analysis/1.0/Email Activities API
  slug: eloqua-reporting-campaignanalysis-1-0-emailactivities-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/CampaignAnalysis/1.0/EmailAsset category.
  name: Oracle Eloqua Reporting/Campaign Analysis/1.0/Email Asset API
  slug: eloqua-reporting-campaignanalysis-1-0-emailasset-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/CampaignAnalysis/1.0/ExternalActivityTotals category.
  name: Oracle Eloqua Reporting/Campaign Analysis/1.0/External Activity Totals API
  slug: eloqua-reporting-campaignanalysis-1-0-externalactivitytotals-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/CampaignAnalysis/1.0/FormActivities category.
  name: Oracle Eloqua Reporting/Campaign Analysis/1.0/Form Activities API
  slug: eloqua-reporting-campaignanalysis-1-0-formactivities-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/CampaignAnalysis/1.0/LandingPageActivities category.
  name: Oracle Eloqua Reporting/Campaign Analysis/1.0/Landing Page Activities API
  slug: eloqua-reporting-campaignanalysis-1-0-landingpageactivities-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/CampaignAnalysis/1.0/LandingPageAsset category.
  name: Oracle Eloqua Reporting/Campaign Analysis/1.0/Landing Page Asset API
  slug: eloqua-reporting-campaignanalysis-1-0-landingpageasset-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/CampaignAnalysis/1.0/LeadActivities category.
  name: Oracle Eloqua Reporting/Campaign Analysis/1.0/Lead Activities API
  slug: eloqua-reporting-campaignanalysis-1-0-leadactivities-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/CampaignAnalysis/1.0/MarketingActivities category.
  name: Oracle Eloqua Reporting/Campaign Analysis/1.0/Marketing Activities API
  slug: eloqua-reporting-campaignanalysis-1-0-marketingactivities-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/CampaignAnalysis/1.0/Segment category.
  name: Oracle Eloqua Reporting/Campaign Analysis/1.0/Segment API
  slug: eloqua-reporting-campaignanalysis-1-0-segment-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/CampaignAnalysis/1.0/User category.
  name: Oracle Eloqua Reporting/Campaign Analysis/1.0/User API
  slug: eloqua-reporting-campaignanalysis-1-0-user-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/CampaignAnalysis/1.0/WebActivities category.
  name: Oracle Eloqua Reporting/Campaign Analysis/1.0/Web Activities API
  slug: eloqua-reporting-campaignanalysis-1-0-webactivities-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/CampaignExternalActivity/1.0/ExternalActivities category.
  name: Oracle Eloqua Reporting/Campaign External Activity/1.0/External Activities API
  slug: eloqua-reporting-campaignexternalactivity-1-0-externalactivities-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/CampaignExternalActivity/1.0/ExternalActivityAttributes category.
  name: Oracle Eloqua Reporting/Campaign External Activity/1.0/External Activity Attributes API
  slug: eloqua-reporting-campaignexternalactivity-1-0-externalactivityattributes-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/FormSubmission/1.0/Calendar category.
  name: Oracle Eloqua Reporting/Form Submission/1.0/Calendar API
  slug: eloqua-reporting-formsubmission-1-0-calendar-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/FormSubmission/1.0/Campaign category.
  name: Oracle Eloqua Reporting/Form Submission/1.0/Campaign API
  slug: eloqua-reporting-formsubmission-1-0-campaign-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/FormSubmission/1.0/EmailAsset category.
  name: Oracle Eloqua Reporting/Form Submission/1.0/Email Asset API
  slug: eloqua-reporting-formsubmission-1-0-emailasset-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/FormSubmission/1.0/FormAsset category.
  name: Oracle Eloqua Reporting/Form Submission/1.0/Form Asset API
  slug: eloqua-reporting-formsubmission-1-0-formasset-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/FormSubmission/1.0/FormSubmissionActivities category.
  name: Oracle Eloqua Reporting/Form Submission/1.0/Form Submission Activities API
  slug: eloqua-reporting-formsubmission-1-0-formsubmissionactivities-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/FormSubmission/1.0/LandingPageAsset category.
  name: Oracle Eloqua Reporting/Form Submission/1.0/Landing Page Asset API
  slug: eloqua-reporting-formsubmission-1-0-landingpageasset-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/FormSubmission/1.0/User category.
  name: Oracle Eloqua Reporting/Form Submission/1.0/User API
  slug: eloqua-reporting-formsubmission-1-0-user-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/FormSubmission/1.0/WebPage category.
  name: Oracle Eloqua Reporting/Form Submission/1.0/Web Page API
  slug: eloqua-reporting-formsubmission-1-0-webpage-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/LandingPageAnalysis/1.0/Calendar category.
  name: Oracle Eloqua Reporting/Landing Page Analysis/1.0/Calendar API
  slug: eloqua-reporting-landingpageanalysis-1-0-calendar-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/LandingPageAnalysis/1.0/LandingPageActivity category.
  name: Oracle Eloqua Reporting/Landing Page Analysis/1.0/Landing Page Activity API
  slug: eloqua-reporting-landingpageanalysis-1-0-landingpageactivity-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/LandingPageAnalysis/1.0/LandingPageAsset category.
  name: Oracle Eloqua Reporting/Landing Page Analysis/1.0/Landing Page Asset API
  slug: eloqua-reporting-landingpageanalysis-1-0-landingpageasset-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/OpportunityAnalysis/1.0/Account category.
  name: Oracle Eloqua Reporting/Opportunity Analysis/1.0/Account API
  slug: eloqua-reporting-opportunityanalysis-1-0-account-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/OpportunityAnalysis/1.0/AccountCampaignScore category.
  name: Oracle Eloqua Reporting/Opportunity Analysis/1.0/Account Campaign Score API
  slug: eloqua-reporting-opportunityanalysis-1-0-accountcampaignscore-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/OpportunityAnalysis/1.0/AccountEngagement category.
  name: Oracle Eloqua Reporting/Opportunity Analysis/1.0/Account Engagement API
  slug: eloqua-reporting-opportunityanalysis-1-0-accountengagement-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/OpportunityAnalysis/1.0/Contact category.
  name: Oracle Eloqua Reporting/Opportunity Analysis/1.0/Contact API
  slug: eloqua-reporting-opportunityanalysis-1-0-contact-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/OpportunityAnalysis/1.0/Opportunity category.
  name: Oracle Eloqua Reporting/Opportunity Analysis/1.0/Opportunity API
  slug: eloqua-reporting-opportunityanalysis-1-0-opportunity-api
- baseURL: https://secure.p01.eloqua.com/API/REST/2.0/
  baseurl_source: declared
  description: The operations from the Reporting/OpportunityAnalysis/1.0/OpportunityRevenue category.
  name: Oracle Eloqua Reporting/Opportunity Analysis/1.0/Opportunity Revenue API
  slug: eloqua-reporting-opportunityanalysis-1-0-opportunityrevenue-api
artifact_total: 195
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Oracle Eloqua Bulk Account Exports API
  slug: open-eloqua-account-exports-api
- collection_type: open
  name: Oracle Eloqua Bulk Account Exports Account Fields API
  slug: open-eloqua-account-fields-api
- collection_type: open
  name: Oracle Eloqua Bulk Account Exports Account Imports API
  slug: open-eloqua-account-imports-api
- collection_type: open
  name: Oracle Eloqua Bulk Account Exports Accounts API
  slug: open-eloqua-accounts-api
- collection_type: open
  name: Oracle Eloqua Bulk Account Exports Activity Exports API
  slug: open-eloqua-activity-exports-api
- collection_type: open
  name: Oracle Eloqua Bulk Account Exports Activity Imports API
  slug: open-eloqua-activity-imports-api
- collection_type: open
  name: Oracle Eloqua Bulk API
  slug: open-eloqua-bulk
- collection_type: open
  name: Oracle Eloqua Bulk Account Exports Campaigns API
  slug: open-eloqua-campaigns-api
- collection_type: open
  name: Oracle Eloqua Bulk Account Exports Contact Exports API
  slug: open-eloqua-contact-exports-api
- collection_type: open
  name: Oracle Eloqua Bulk Account Exports Contact Fields API
  slug: open-eloqua-contact-fields-api
- collection_type: open
  name: Oracle Eloqua Bulk Account Exports Contact Imports API
  slug: open-eloqua-contact-imports-api
- collection_type: open
  name: Oracle Eloqua Bulk Account Exports Contact Lists API
  slug: open-eloqua-contact-lists-api
- collection_type: open
  name: Oracle Eloqua Bulk Account Exports Contact Segments API
  slug: open-eloqua-contact-segments-api
- collection_type: open
  name: Oracle Eloqua Bulk Account Exports Contacts API
  slug: open-eloqua-contacts-api
- collection_type: open
  name: Oracle Eloqua Bulk Account Exports Custom Object Exports API
  slug: open-eloqua-custom-object-exports-api
- collection_type: open
  name: Oracle Eloqua Bulk Account Exports Custom Object Imports API
  slug: open-eloqua-custom-object-imports-api
- collection_type: open
  name: Oracle Eloqua Bulk Account Exports Custom Objects API
  slug: open-eloqua-custom-objects-api
- collection_type: open
  name: Oracle Eloqua Bulk Account Exports Emails API
  slug: open-eloqua-emails-api
- collection_type: open
  name: Oracle Eloqua Bulk Account Exports Forms API
  slug: open-eloqua-forms-api
- collection_type: open
  name: Oracle Eloqua Bulk Account Exports Landing Pages API
  slug: open-eloqua-landing-pages-api
- collection_type: open
  name: Oracle Eloqua Bulk Account Exports Programs API
  slug: open-eloqua-programs-api
- collection_type: open
  name: Oracle Eloqua REST API
  slug: open-eloqua-rest
- collection_type: open
  name: Oracle Eloqua Bulk Account Exports Syncs API
  slug: open-eloqua-syncs-api
- collection_type: open
  name: Oracle Eloqua Bulk Account Exports Users API
  slug: open-eloqua-users-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/eloqua-capability-edges.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/oracle/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- group: company
  title: ''
  type: Website
  url: https://www.oracle.com/cx/marketing/automation/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/en/cloud/saas/marketing/eloqua-develop/
- group: start
  title: ''
  type: SignUp
  url: https://login.eloqua.com/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eloqua-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eloqua-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eloqua-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/eloqua-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eloqua
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oracle.com/en/cloud/saas/marketing/eloqua-rest-api/Getting_Started_Application.html
- group: auth
  title: ''
  type: Authentication
  url: https://docs.oracle.com/en/cloud/saas/marketing/eloqua-rest-api/Authentication.html
- group: operate
  title: ''
  type: Support
  url: https://support.oracle.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.oracle.com/en/cloud/saas/marketing/eloqua-rest-api/rest-endpoints.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.oracle.com/en/cloud/saas/marketing/eloqua-develop/
- group: build
  title: ''
  type: Packages
  url: packages/eloqua-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eloqua-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/eloqua-published-swagger-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/eloqua-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/eloqua-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/eloqua-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://community.oracle.com/customerconnect/categories/cx-eloqua-system-status/
- group: design
  title: ''
  type: Conventions
  url: conventions/eloqua-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/eloqua-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/eloqua-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/eloqua-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/eloqua-rate-limits.yml
created: '2025-01-01'
description: Oracle Eloqua is a marketing automation platform that provides tools for lead management, email marketing, and marketing campaign management through comprehensive REST APIs. It enables marketing teams to create, execute, and measure the effectiveness of marketing programs and campaigns.
finops:
- name: Eloqua Finops
  service_category: API
  slug: eloqua-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eloqua.png
json_schemas:
- name: Eloqua Campaign
  property_count: 20
  slug: eloqua-campaign
- name: Eloqua Contact
  property_count: 36
  slug: eloqua-contact
- name: Eloqua Email
  property_count: 39
  slug: eloqua-email
jsonld:
- class_count: 0
  name: Eloqua Context
  property_count: 10
  slug: eloqua-context
layout: provider
modified: '2026-08-21'
name: Oracle Eloqua
nav: Providers
network: true
overview: 'Oracle Eloqua publishes 158 APIs on the [APIs.io](https://apis.io/) network, including Account Exports API, Account Fields API, Account Imports API, and 155 more. Tagged areas include CRM, Email Marketing, Lead Management, Marketing Automation, and Campaign Management.


  The Oracle Eloqua catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Oracle Eloqua''s developer surface includes documentation, signup flow, authentication, getting-started guide, support, API reference, changelog, and 24 more developer resources.'
plans:
- name: Eloqua Plans Pricing
  plan_count: 0
  slug: eloqua-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 4
  name: Eloqua Rate Limits
  slug: eloqua-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Oracle Eloqua API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: eloqua-jsonschema-spectral-rules
scopes:
- name: Eloqua Scopes
  scope_count: 1
  slug: eloqua-scopes
  summary_line: 1 scope · authorizationCode/implicit/password
score:
  band: developing
  composite: 49.8
  coverage:
    artifact_dirs: 26
    catalog_earned: 63.3
    catalog_earned_first_party: 12.0
    catalog_gap: 51.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 14.4
    contract_quality: 53.0
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 14.4
    operational_transparency: 57.9
  previous_composite: 49.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 13.9
      derived: 0
      marker_coverage: 0.0
      total: 158
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eloqua/refs/heads/main/screenshots/eloqua-2026-06-20T180617.png
security:
- kind: authentication
  name: Eloqua Authentication
  slug: eloqua-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Eloqua Domain Security
  slug: eloqua-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: eloqua
tags:
- CRM
- Email Marketing
- Lead Management
- Marketing Automation
- Campaign Management
- Bulk Data
- Landing Pages
- Forms
- Reporting
- B2B Marketing
website: https://www.oracle.com/cx/marketing/automation/
---
