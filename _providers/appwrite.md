---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 54.5
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 665
  human_in_the_loop: 7
  name: Appwrite Agentic Access
  operation_count: 1022
  slug: appwrite-agentic-access
  summary_line: 1022 operations · 665 acting · 7 human-in-the-loop
api_count: 2
apis:
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The Project service allows you to manage all the projects in your Appwrite server. 109 operations across 97 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Project API
  phrasing_intents:
  - id: projectGet
    intent: Get the current project's details
    question: What are the settings and details of the project my key belongs to?
  - id: projectDelete
    intent: Delete the whole project
    question: Can I permanently delete my entire Appwrite project?
  - id: projectUpdateAuthMethod
    intent: Enable or disable a sign-in method
    question: Can I turn off email/password or anonymous login for my project?
  - id: projectListKeys
    intent: List the project's API keys
    question: Which API keys exist on my project?
  - id: projectCreateKey
    intent: Create a long-lived scoped API key
    question: How do I create a server API key with only the scopes it needs?
  - id: projectCreateEphemeralKey
    intent: Create a short-lived ephemeral API key
    question: Can I mint a temporary API key that expires within an hour?
  - id: projectGetKey
    intent: Get one API key
    question: What scopes and expiry does a specific API key have?
  - id: projectUpdateKey
    intent: Rename or rescope an API key
    question: Can I change the scopes on an API key I already created?
  phrasing_ops: 109
  slug: appwrite-project-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The TablesDB service allows you to create structured tables of columns, query and filter lists of rows. 80 operations across 59 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite TablesDB API
  phrasing_intents:
  - id: tablesDBList
    intent: List TablesDB databases in a project
    question: Which TablesDB databases exist in my Appwrite project?
  - id: tablesDBCreate
    intent: Create a TablesDB database
    question: How do I create a new TablesDB database?
  - id: tablesDBListSpecifications
    intent: List dedicated TablesDB compute specifications
    question: What dedicated database sizes can I use for TablesDB on my current plan?
  - id: tablesDBListTransactions
    intent: List TablesDB transactions
    question: Which transactions are currently open across my TablesDB databases?
  - id: tablesDBCreateTransaction
    intent: Start a TablesDB transaction
    question: How do I start a transaction so several row changes apply together in TablesDB?
  - id: tablesDBGetTransaction
    intent: Get a TablesDB transaction
    question: What state is a specific TablesDB transaction in?
  - id: tablesDBUpdateTransaction
    intent: Commit or roll back a TablesDB transaction
    question: How do I commit a TablesDB transaction once all its operations are staged?
  - id: tablesDBDeleteTransaction
    intent: Delete a TablesDB transaction
    question: How do I delete a TablesDB transaction I no longer need?
  phrasing_ops: 80
  slug: appwrite-tablesdb-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The Account service allows you to authenticate and manage a user account. 73 operations across 47 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Account API
  phrasing_intents:
  - id: accountGet
    intent: Get the signed-in user's account
    question: Who is the user currently logged in to my Appwrite app?
  - id: accountCreate
    intent: Register a new user account
    question: How do I let a new user sign up with an email and password?
  - id: accountDelete
    intent: Delete the signed-in user's account
    question: Can a logged-in user delete their own account?
  - id: accountListBillingAddresses
    intent: List the account's billing addresses
    question: Which billing addresses are saved on my account?
  - id: accountCreateBillingAddress
    intent: Add a billing address to the account
    question: How do I add a new billing address to my account?
  - id: accountGetBillingAddress
    intent: Get one billing address by ID
    question: Can I look up a single saved billing address by its ID?
  - id: accountUpdateBillingAddress
    intent: Update an existing billing address
    question: How do I change a billing address I already saved?
  - id: accountDeleteBillingAddress
    intent: Delete a billing address
    question: Can I remove an old billing address from my account?
  phrasing_ops: 73
  slug: appwrite-account-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The Databases service allows you to create structured collections of documents, query and filter lists of documents. 70 operations across 51 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Databases API
  phrasing_intents:
  - id: databasesList
    intent: List databases in the project
    question: Which databases exist in my Appwrite project?
  - id: databasesCreate
    intent: Create a database
    question: How do I create a new database to hold my app's collections?
  - id: databasesListTransactions
    intent: List transactions across all databases
    question: Which database transactions are currently open in my project?
  - id: databasesCreateTransaction
    intent: Start a database transaction
    question: How do I make several document writes succeed or fail together?
  - id: databasesGetTransaction
    intent: Get a database transaction
    question: What is the status of a particular transaction?
  - id: databasesUpdateTransaction
    intent: Commit or roll back a database transaction
    question: How do I commit all the operations staged in a transaction?
  - id: databasesDeleteTransaction
    intent: Delete a database transaction
    question: How do I delete a transaction record I no longer need?
  - id: databasesCreateOperations
    intent: Stage multiple operations in a transaction
    question: Can I add a batch of document operations to an open transaction in one call?
  phrasing_ops: 70
  slug: appwrite-databases-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: Appwrite Domains — buy domains and host DNS inside an Appwrite organization, announced 2026-09-04. 54 operations across 44 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Domains API
  phrasing_intents:
  - id: domainsList
    intent: List the project's domains
    question: Which domains are registered in my Appwrite project?
  - id: domainsCreate
    intent: Add a domain to a team
    question: How do I add a domain I already own so I can manage its DNS here?
  - id: domainsGetPrice
    intent: Get the registration price for one domain
    question: How much does it cost to register a single domain name?
  - id: domainsListPrices
    intent: Check availability and prices for several domains
    question: Are these domain names available, and what would each cost?
  - id: domainsCreatePurchase
    intent: Start buying a domain
    question: How do I buy a new domain name and pay for it with a saved card?
  - id: domainsUpdatePurchase
    intent: Confirm and finalize a domain purchase
    question: How do I finish a domain purchase after completing 3D Secure?
  - id: domainsListSuggestions
    intent: Suggest available domain names
    question: Can you suggest domain names based on a keyword?
  - id: domainsCreateTransferIn
    intent: Start transferring a domain in
    question: How do I move a domain from another registrar into Appwrite?
  phrasing_ops: 54
  slug: appwrite-domains-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The Messaging service allows you to send messages to any provider type (SMTP, push notification, SMS, etc.). 46 operations across 39 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Messaging API
  phrasing_intents:
  - id: messagingListMessages
    intent: List sent and scheduled messages
    question: Which emails, SMS and push notifications has my Appwrite project sent?
  - id: messagingCreateEmail
    intent: Send or schedule an email message
    question: How do I send an email to everyone subscribed to a topic?
  - id: messagingUpdateEmail
    intent: Edit a draft email message
    question: Can I change the subject of an email that is still a draft?
  - id: messagingCreatePush
    intent: Send or schedule a push notification
    question: How do I send a push notification to a user's devices?
  - id: messagingUpdatePush
    intent: Edit a draft push notification
    question: Can I change the title of a push notification before it goes out?
  - id: messagingCreateSms
    intent: Send or schedule an SMS
    question: How do I send a text message to users in my app?
  - id: messagingUpdateSms
    intent: Edit a draft SMS
    question: Can I fix the wording of a text message that is still a draft?
  - id: messagingGetMessage
    intent: Get one message
    question: Did a particular message get delivered or fail?
  phrasing_ops: 46
  slug: appwrite-messaging-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The Organizations service allows you to manage organization billing, plans, invoices, and add-ons. 45 operations across 38 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Organizations API
  phrasing_intents:
  - id: organizationsList
    intent: List organizations I belong to
    question: Which Appwrite organizations am I a member of?
  - id: organizationsCreate
    intent: Create a new billed organization
    question: How do I create a new organization on a paid billing plan?
  - id: organizationsEstimationCreateOrganization
    intent: Estimate the cost of a new organization
    question: What would it cost to open a new organization on a given plan before I commit?
  - id: organizationsDelete
    intent: Delete an organization
    question: How do I delete one of my organizations entirely?
  - id: organizationsListAddons
    intent: List an organization's billing addons
    question: Which paid addons are active on my organization?
  - id: organizationsCreateBaaAddon
    intent: Add the BAA addon to an organization
    question: How do I get a Business Associate Agreement for HIPAA workloads on my organization?
  - id: organizationsCreatePremiumGeoDBAddon
    intent: Add the Premium Geo DB addon
    question: How do I turn on the Premium Geo DB addon for more detailed geolocation?
  - id: organizationsGetAddon
    intent: Get a billing addon's details
    question: What is the status of a specific addon on my organization?
  phrasing_ops: 45
  slug: appwrite-organizations-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The Users service allows you to manage your project users. 45 operations across 35 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Users API
  phrasing_intents:
  - id: usersList
    intent: List the project's users
    question: Who are all the users registered in my project?
  - id: usersCreate
    intent: Create a user
    question: How do I add a new user to my project from the server side?
  - id: usersCreateArgon2User
    intent: Import a user with an Argon2-hashed password
    question: How do I import a user whose password is already hashed with Argon2?
  - id: usersCreateBcryptUser
    intent: Import a user with a bcrypt-hashed password
    question: Can I bring over users whose passwords are stored as bcrypt hashes?
  - id: usersListIdentities
    intent: List OAuth identities across all users
    question: Which OAuth identities are linked to users in my project?
  - id: usersDeleteIdentity
    intent: Unlink an OAuth identity
    question: How do I disconnect a social login identity from a user?
  - id: usersCreateMD5User
    intent: Import a user with an MD5-hashed password
    question: How do I import legacy users whose passwords are MD5 hashes?
  - id: usersCreatePHPassUser
    intent: Import a user with a PHPass-hashed password
    question: Can I migrate users from a PHP app whose passwords are PHPass hashes?
  phrasing_ops: 45
  slug: appwrite-users-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: Managed PostgreSQL hosting with pgvector, Prisma support, backups, replicas and point-in-time recovery. 37 operations across 25 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite PostgreSQL API
  phrasing_intents:
  - id: postgresqlList
    intent: List dedicated databases
    question: Which dedicated PostgreSQL databases do I have running in Appwrite?
  - id: postgresqlCreate
    intent: Provision a dedicated database
    question: How do I spin up a new dedicated Postgres database?
  - id: postgresqlListSpecifications
    intent: List database sizes and prices on my plan
    question: What CPU, memory and storage sizes can I pick for a dedicated database?
  - id: postgresqlGet
    intent: Get a dedicated database's configuration
    question: Is my new database still provisioning or ready to use?
  - id: postgresqlUpdate
    intent: Change a dedicated database's configuration
    question: Can I resize a database's CPU and memory without downtime?
  - id: postgresqlDelete
    intent: Delete a dedicated database
    question: How do I permanently tear down a dedicated database?
  - id: postgresqlListBackups
    intent: List a database's backups
    question: What backups exist for my dedicated database?
  - id: postgresqlCreateBackup
    intent: Take a manual database backup
    question: Can I take an on-demand backup of a database before a risky change?
  phrasing_ops: 37
  slug: appwrite-postgresql-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: DocumentsDB — schemaless document storage with documents that evolve with the application, announced 2026-09-02. 36 operations across 18 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite DocumentsDB API
  phrasing_intents:
  - id: documentsDBList
    intent: List document databases in the project
    question: Which DocumentsDB databases exist in my project?
  - id: documentsDBCreate
    intent: Create a document database
    question: How do I create a new document database?
  - id: documentsDBListSpecifications
    intent: List dedicated database plans and prices
    question: What dedicated database sizes can I choose on my plan?
  - id: documentsDBListTransactions
    intent: List database transactions
    question: Which transactions are currently open across my databases?
  - id: documentsDBCreateTransaction
    intent: Start a database transaction
    question: How do I start a transaction so several document writes succeed or fail together?
  - id: documentsDBGetTransaction
    intent: Get a transaction's details
    question: What state is a specific transaction in?
  - id: documentsDBUpdateTransaction
    intent: Commit or roll back a transaction
    question: How do I commit the staged changes in a transaction?
  - id: documentsDBDeleteTransaction
    intent: Delete a transaction
    question: How do I throw away a transaction record entirely?
  phrasing_ops: 36
  slug: appwrite-documentsdb-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: VectorsDB — similarity search as a first-class Appwrite database, announced 2026-09-02. 35 operations across 17 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite VectorsDB API
  phrasing_intents:
  - id: vectorsDBList
    intent: List vector databases in the project
    question: Which vector databases exist in my Appwrite project?
  - id: vectorsDBCreate
    intent: Create a vector database
    question: How do I create a new database for storing embeddings?
  - id: vectorsDBListSpecifications
    intent: List dedicated vector database plans and prices
    question: What dedicated database specifications can I choose from on my current plan?
  - id: vectorsDBListTransactions
    intent: List transactions across vector databases
    question: Which transactions are open across my vector databases?
  - id: vectorsDBCreateTransaction
    intent: Start a vector database transaction
    question: How do I group several vector document writes into one atomic transaction?
  - id: vectorsDBGetTransaction
    intent: Get a vector database transaction
    question: What is the current state of a specific vector database transaction?
  - id: vectorsDBUpdateTransaction
    intent: Commit or roll back a vector database transaction
    question: How do I commit the staged operations in a vector database transaction?
  - id: vectorsDBDeleteTransaction
    intent: Delete a vector database transaction
    question: How do I discard a vector database transaction record entirely?
  phrasing_ops: 35
  slug: appwrite-vectorsdb-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: Managed MySQL databases — bring your own MySQL or run Appwrite-hosted instances, announced 2026-09-02. 34 operations across 23 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite MySQL API
  phrasing_intents:
  - id: mysqlList
    intent: List dedicated MySQL databases
    question: Which dedicated MySQL databases do I have running?
  - id: mysqlCreate
    intent: Provision a dedicated MySQL database
    question: How do I spin up a dedicated MySQL database in Appwrite?
  - id: mysqlListSpecifications
    intent: List available database sizes and prices
    question: What CPU, memory and storage sizes can I pick for a dedicated database?
  - id: mysqlGet
    intent: Get a dedicated database's configuration
    question: What configuration is a dedicated database running with?
  - id: mysqlUpdate
    intent: Change a dedicated database's settings
    question: Can I resize a dedicated database without downtime?
  - id: mysqlDelete
    intent: Delete a dedicated MySQL database
    question: How do I permanently delete a dedicated MySQL database?
  - id: mysqlListBackups
    intent: List a database's backups
    question: What backups exist for my dedicated database?
  - id: mysqlCreateBackup
    intent: Take a manual database backup
    question: How do I take an on-demand backup of a dedicated database?
  phrasing_ops: 34
  slug: appwrite-mysql-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: Managed MongoDB databases, with backup policies, archives and restorations. 31 operations across 21 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite MongoDB API
  phrasing_intents:
  - id: mongoList
    intent: List dedicated Mongo databases
    question: Which dedicated Mongo databases do I have in Appwrite?
  - id: mongoCreate
    intent: Provision a dedicated Mongo database
    question: How do I spin up a dedicated Mongo database?
  - id: mongoListSpecifications
    intent: List dedicated Mongo compute specifications
    question: What Mongo database sizes can I choose on my current plan?
  - id: mongoGet
    intent: Get a dedicated Mongo database
    question: What is the configuration and status of my Mongo database?
  - id: mongoUpdate
    intent: Update a dedicated Mongo database's configuration
    question: Can I pause a Mongo database and resume it later?
  - id: mongoDelete
    intent: Delete a dedicated Mongo database
    question: How do I permanently delete a dedicated Mongo database?
  - id: mongoListBackups
    intent: List backups of a Mongo database
    question: Which backups exist for my Mongo database?
  - id: mongoCreateBackup
    intent: Take a manual backup of a Mongo database
    question: How do I take an on-demand backup of my Mongo database right now?
  phrasing_ops: 31
  slug: appwrite-mongo-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The Functions Service allows you view, create and manage your Cloud Functions. 28 operations across 18 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Functions API
  phrasing_intents:
  - id: functionsList
    intent: List the project's functions
    question: What serverless functions are defined in my Appwrite project?
  - id: functionsCreate
    intent: Create a serverless function
    question: How do I create a new cloud function with a chosen runtime?
  - id: functionsListRuntimes
    intent: List available function runtimes
    question: Which languages and runtime versions can my functions use?
  - id: functionsListSpecifications
    intent: List allowed function compute specs
    question: What CPU and memory sizes can I give a function?
  - id: functionsListTemplates
    intent: Browse function templates
    question: Are there ready-made function templates I can start from?
  - id: functionsGetTemplate
    intent: Get one function template
    question: What does a specific function template include before I use it?
  - id: functionsGet
    intent: Get a function's configuration
    question: How do I view the settings of one function, like its runtime and timeout?
  - id: functionsUpdate
    intent: Update a function's settings
    question: Can I change the timeout or schedule of an existing function?
  phrasing_ops: 28
  slug: appwrite-functions-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The Sites Service allows you view, create and manage your web applications. 27 operations across 18 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Sites API
  phrasing_intents:
  - id: sitesList
    intent: List the project's sites
    question: Which sites are hosted in my Appwrite project?
  - id: sitesCreate
    intent: Create a new site
    question: How do I create a site for my Next.js or Astro app?
  - id: sitesListFrameworks
    intent: List supported site frameworks
    question: Which web frameworks can I host as a site?
  - id: sitesListSpecifications
    intent: List allowed site compute specifications
    question: What CPU and memory sizes can a site use?
  - id: sitesListTemplates
    intent: Browse site starter templates
    question: Are there starter templates I can deploy a site from?
  - id: sitesGetTemplate
    intent: Get a site template's details
    question: What does a particular site template include?
  - id: sitesGet
    intent: Get a site's configuration
    question: What is the current configuration of one of my sites?
  - id: sitesUpdate
    intent: Update a site's settings
    question: How do I change a site's build command or output directory?
  phrasing_ops: 27
  slug: appwrite-sites-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The Organization service allows you to manage organization-level projects. 23 operations across 9 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Organization API
  phrasing_intents:
  - id: organizationGet
    intent: Get the current organization
    question: What are the details of the organization my key belongs to?
  - id: organizationUpdate
    intent: Rename the current organization
    question: Can I change the name of my organization?
  - id: organizationDelete
    intent: Delete the current organization
    question: Does deleting my organization also delete every project inside it?
  - id: organizationListInstallations
    intent: List apps installed on the organization
    question: Which apps are installed on my organization?
  - id: organizationCreateInstallation
    intent: Install an app on the organization
    question: How do I install an app on my organization?
  - id: organizationGetInstallation
    intent: Get one app installation
    question: What scopes does a specific app installation on my organization hold?
  - id: organizationUpdateInstallation
    intent: Refresh an app installation's scopes
    question: When an app starts requesting new scopes, how do I refresh what its installation is granted?
  - id: organizationDeleteInstallation
    intent: Uninstall an app from the organization
    question: How do I uninstall an app from my organization?
  phrasing_ops: 23
  slug: appwrite-organization-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The Apps service allows you to manage OAuth2 applications, their keys, secrets, scopes, and installations. 22 operations across 14 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Apps API
  phrasing_intents:
  - id: appsList
    intent: List OAuth2 applications
    question: Which third-party applications have I registered in Appwrite?
  - id: appsCreate
    intent: Register a new OAuth2 application
    question: How do I register an application that users can sign in to with OAuth2?
  - id: appsListInstallationScopes
    intent: List scopes an app can request on team install
    question: What permissions can an application ask for when it is installed on a team?
  - id: appsListOAuth2Scopes
    intent: List scopes an app can request during OAuth2
    question: What scopes can my application request from users during the OAuth2 sign-in flow?
  - id: appsGet
    intent: Get an application's details
    question: What redirect URIs and settings does a particular application have?
  - id: appsUpdate
    intent: Update an application's settings
    question: How do I change the redirect URIs of an application I already registered?
  - id: appsDelete
    intent: Delete an application
    question: How do I permanently remove a registered application?
  - id: appsListInstallations
    intent: List the teams where an app is installed
    question: Which teams have installed my application?
  phrasing_ops: 22
  slug: appwrite-apps-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The Console service allows you to interact with console relevant information. 19 operations across 19 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Console API
  phrasing_intents:
  - id: consoleGetCampaign
    intent: Get a marketing campaign's details
    question: What does a particular console campaign offer?
  - id: consoleGetCoupon
    intent: Look up a coupon code in the console
    question: Is a coupon code valid, and what credit does it give?
  - id: consoleListDatabases
    intent: List every database in the project
    question: Can I see all my project's databases across every type in one call?
  - id: consoleListOAuth2Providers
    intent: List supported OAuth2 login providers
    question: Which OAuth2 providers can I enable for sign-in?
  - id: consoleGetPlans
    intent: List available billing plans
    question: What billing plans are available?
  - id: consoleGetPlan
    intent: Get one billing plan's details
    question: What limits and pricing come with a specific plan?
  - id: consoleListPostgresExtensions
    intent: List installable Postgres extensions
    question: Which Postgres extensions can I install on a dedicated database?
  - id: consoleGetProgram
    intent: Get a program's details
    question: What does a console program such as a startup program include?
  phrasing_ops: 19
  slug: appwrite-console-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: Console management surface for project-level WAF rules and operator tooling. 19 operations across 18 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Manager API
  phrasing_intents:
  - id: managerCreateBlock
    intent: Block a resource type for a project
    question: How do I block a project from using a certain resource type?
  - id: managerDeleteBlock
    intent: Lift resource blocks on a project
    question: Can I remove a block I placed on a project's resources?
  - id: managerListBlocks
    intent: List resource blocks on a project
    question: Which resources are currently blocked for a given project?
  - id: managerDeleteCache
    intent: Clear the internal cache
    question: How do I flush the internal cache for one project?
  - id: managerUpdateDatabase
    intent: Report a database container's status
    question: How does Edge tell Cloud that a database container spun down?
  - id: managerCreateDatabaseActivity
    intent: Sync database last-active timestamps in bulk
    question: How are last-active times for many databases synced in one call?
  - id: managerCreateDatabaseMetrics
    intent: Submit dedicated database metrics in bulk
    question: How do I report CPU, memory and storage readings for dedicated databases?
  - id: managerCreateDatabaseEvent
    intent: Send a database lifecycle event
    question: How does Edge notify Cloud that a database failover or provisioning finished?
  phrasing_ops: 19
  slug: appwrite-manager-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The Teams service allows you to group users of your project and to enable them to share read and write access to your project resources. 19 operations across 9 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Teams API
  phrasing_intents:
  - id: teamsList
    intent: List the teams I belong to
    question: Which teams is the current user a member of?
  - id: teamsCreate
    intent: Create a team
    question: How do I create a team in Appwrite?
  - id: teamsGet
    intent: Get a team
    question: What are the details of a specific team?
  - id: teamsUpdateName
    intent: Rename a team
    question: How do I rename a team?
  - id: teamsDelete
    intent: Delete a team
    question: How do I delete a team entirely?
  - id: teamsListInstallations
    intent: List apps installed on a team
    question: Which apps are installed on my team?
  - id: teamsCreateInstallation
    intent: Install an app on a team
    question: How do I install an app on a team?
  - id: teamsGetInstallation
    intent: Get an app installation on a team
    question: What scopes were granted to a specific app installation on my team?
  phrasing_ops: 19
  slug: appwrite-teams-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The Project service allows you to manage all the projects in your Appwrite server. 18 operations across 14 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Projects API
  phrasing_intents:
  - id: projectsListAddons
    intent: List a project's billing addons
    question: Which paid addons are active on my Appwrite project?
  - id: projectsCreatePremiumGeoDBAddon
    intent: Add the Premium Geo DB addon to a project
    question: How do I turn on the Premium Geo DB addon for a project?
  - id: projectsGetAddon
    intent: Get one project addon
    question: What are the details of a specific billing addon on my project?
  - id: projectsDeleteAddon
    intent: Remove a billing addon from a project
    question: How do I cancel a paid addon on one of my projects?
  - id: projectsConfirmAddonPayment
    intent: Confirm an addon payment after 3DS
    question: My addon purchase asked for 3D Secure, how do I finish the payment?
  - id: projectsGetAddonPrice
    intent: Check what an addon will cost a project
    question: How much will an addon cost if I add it partway through my billing cycle?
  - id: projectsUpdateConsoleAccess
    intent: Record console access to a project
    question: How does the console track when a project was last opened?
  - id: projectsListDevKeys
    intent: List a project's dev keys
    question: Which dev keys exist for my project?
  phrasing_ops: 18
  slug: appwrite-projects-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The Migrations service allows you to migrate third-party data to your Appwrite project. 16 operations across 14 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Migrations API
  phrasing_intents:
  - id: migrationsList
    intent: List migrations in the project
    question: What migrations have run in my project, and did any of them fail?
  - id: migrationsCreateAppwriteMigration
    intent: Migrate data from another Appwrite project
    question: How do I copy databases, users and files from one Appwrite project into another?
  - id: migrationsGetAppwriteReport
    intent: Preview an Appwrite-to-Appwrite migration
    question: Before migrating from another Appwrite project, how can I see which resources it holds?
  - id: migrationsCreateCSVExport
    intent: Export collection documents to a CSV file
    question: How do I export a collection's documents to a CSV file?
  - id: migrationsCreateCSVImport
    intent: Import documents from a CSV file
    question: How do I load rows from a CSV file in Storage into a database collection?
  - id: migrationsCreateFirebaseMigration
    intent: Migrate a Firebase project into Appwrite
    question: How do I move my Firebase users and data into Appwrite?
  - id: migrationsGetFirebaseReport
    intent: Preview a Firebase migration
    question: Before migrating off Firebase, can I see which resources would be brought over?
  - id: migrationsCreateJSONExport
    intent: Export collection documents to a JSON file
    question: How do I export a collection's documents as JSON?
  phrasing_ops: 16
  slug: appwrite-migrations-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The Storage service allows you to manage your project files. 13 operations across 7 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Storage API
  phrasing_intents:
  - id: storageListBuckets
    intent: List storage buckets
    question: Which storage buckets exist in my project?
  - id: storageCreateBucket
    intent: Create a storage bucket
    question: How do I create a bucket to hold uploaded files?
  - id: storageGetBucket
    intent: Get a bucket's settings
    question: What limits and permissions are set on a bucket?
  - id: storageUpdateBucket
    intent: Change an existing bucket's settings
    question: Can I turn on compression or antivirus for a bucket I already have?
  - id: storageDeleteBucket
    intent: Delete a storage bucket
    question: How do I delete a bucket I no longer use?
  - id: storageListFiles
    intent: List files in a bucket
    question: Which files are stored in a bucket?
  - id: storageCreateFile
    intent: Upload a file to a bucket
    question: How do I upload a file into a storage bucket?
  - id: storageGetFile
    intent: Get a file's metadata
    question: What size and type is a stored file?
  phrasing_ops: 13
  slug: appwrite-storage-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: Appwrite Firewall — traffic control and WAF rules for a project, announced 2026-09-04. 13 operations across 12 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Firewall (WAF) API
  phrasing_intents:
  - id: wafListRules
    intent: List the firewall rules in a project
    question: Which web application firewall rules are active on my Appwrite project?
  - id: wafCreateBypassRule
    intent: Create a firewall rule that lets traffic skip checks
    question: How do I let requests from my office IP range skip the firewall?
  - id: wafUpdateBypassRule
    intent: Edit an existing bypass firewall rule
    question: Can I change the conditions on a bypass rule I already created?
  - id: wafCreateChallengeRule
    intent: Create a proof-of-work challenge firewall rule
    question: How do I make suspicious visitors solve a challenge before reaching my site?
  - id: wafUpdateChallengeRule
    intent: Edit an existing challenge firewall rule
    question: Can I raise the difficulty on a challenge rule that is already live?
  - id: wafCreateDenyRule
    intent: Create a firewall rule that blocks matching traffic
    question: How do I block requests from a specific country or IP range?
  - id: wafUpdateDenyRule
    intent: Edit an existing blocking firewall rule
    question: Can I change which IPs an existing deny rule blocks?
  - id: wafCreateRateLimitRule
    intent: Create a rate-limit firewall rule
    question: How do I cap how many requests a single IP can make per minute?
  phrasing_ops: 13
  slug: appwrite-waf-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The Backups service allows you to manage backup policies, archives, and restorations for your project. 12 operations across 7 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Backups API
  phrasing_intents:
  - id: backupsListArchives
    intent: List the project's backup archives
    question: Which backup archives exist for my project?
  - id: backupsCreateArchive
    intent: Take an on-demand backup archive
    question: How do I take a one-off backup of my project right now?
  - id: backupsGetArchive
    intent: Get a backup archive's details
    question: What's the status and size of one specific backup archive?
  - id: backupsDeleteArchive
    intent: Delete a backup archive
    question: Can I remove an old backup archive to free up space?
  - id: backupsListPolicies
    intent: List scheduled backup policies
    question: Which scheduled backup policies are set up on my project?
  - id: backupsCreatePolicy
    intent: Schedule automatic backups with a retention
    question: How do I schedule automatic daily backups of my databases?
  - id: backupsGetPolicy
    intent: Get a backup policy's configuration
    question: What schedule and retention does one of my backup policies use?
  - id: backupsUpdatePolicy
    intent: Change a backup policy's schedule or retention
    question: Can I change how often an existing backup policy runs?
  phrasing_ops: 12
  slug: appwrite-backups-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The VCS service allows you to interact with providers like GitHub, GitLab etc. 11 operations across 9 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite VCS API
  phrasing_intents:
  - id: vcsCreateRepositoryDetection
    intent: Detect a repository's language and runtime
    question: Can Appwrite work out which runtime a GitHub repository needs before I deploy it?
  - id: vcsListRepositories
    intent: List GitHub repositories on an installation
    question: Which GitHub repositories can my Appwrite installation see?
  - id: vcsCreateRepository
    intent: Create a new GitHub repository
    question: Can I create a brand-new GitHub repository straight from Appwrite?
  - id: vcsGetRepository
    intent: Get one GitHub repository's details
    question: How do I check the visibility and latest push date of one connected repository?
  - id: vcsListRepositoryBranches
    intent: List a repository's branches
    question: Which branches exist in a GitHub repo connected to my project?
  - id: vcsGetRepositoryContents
    intent: Browse files and folders in a repository
    question: How can I see the files and folders inside a connected GitHub repo?
  - id: vcsUpdateExternalDeployments
    intent: Authorize deployments for an outside pull request
    question: How do I allow a pull request from an external contributor to get a preview deployment?
  - id: vcsListInstallations
    intent: List the project's VCS installations
    question: What version control installations are connected to my Appwrite project?
  phrasing_ops: 11
  slug: appwrite-vcs-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The Avatars service aims to help you complete everyday tasks related to your app image, icons, and avatars. 9 operations across 9 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Avatars API
  phrasing_intents:
  - id: avatarsGetBrowser
    intent: Get a browser icon image
    question: How can I show a Chrome or Firefox icon next to each of a user's sessions?
  - id: avatarsGetCreditCard
    intent: Get a credit card brand icon
    question: Can I display the Visa or Mastercard logo for a saved card in my checkout UI?
  - id: avatarsGetFavicon
    intent: Fetch a website's favicon
    question: How do I grab the favicon of any website to show beside a link?
  - id: avatarsGetFlag
    intent: Get a country flag icon
    question: Can I show a country's flag from its two-letter code?
  - id: avatarsGetImage
    intent: Fetch and crop a remote image
    question: How can I crop a remote image from a URL to a thumbnail size for my app?
  - id: avatarsGetInitials
    intent: Generate an initials avatar
    question: How do I show a placeholder avatar with a user's initials?
  - id: avatarsGetPhoto
    intent: Get the best available profile photo
    question: Which sources are tried, in order, when looking up a user's profile photo?
  - id: avatarsGetQR
    intent: Generate a QR code image
    question: How can I turn a piece of text or a link into a QR code image?
  phrasing_ops: 9
  slug: appwrite-avatars-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The Proxy Service allows you to configure actions for your domains beyond DNS configuration. 9 operations across 8 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Proxy API
  phrasing_intents:
  - id: proxyCreateInvalidation
    intent: Purge CDN cache for a domain
    question: How do I clear the CDN cache for my custom domain?
  - id: proxyListRules
    intent: List proxy rules
    question: Which custom domains have proxy rules in my project?
  - id: proxyCreateAPIRule
    intent: Serve the Appwrite API on a custom domain
    question: Can I serve the Appwrite API from my own domain?
  - id: proxyCreateFunctionRule
    intent: Point a custom domain at a function
    question: How do I run an Appwrite Function on a custom domain?
  - id: proxyCreateRedirectRule
    intent: Redirect a custom domain to another URL
    question: How do I redirect one of my domains to another address?
  - id: proxyCreateSiteRule
    intent: Serve an Appwrite Site on a custom domain
    question: How do I connect my own domain to an Appwrite Site?
  - id: proxyGetRule
    intent: Get a proxy rule
    question: What is a specific proxy rule pointing at?
  - id: proxyDeleteRule
    intent: Delete a proxy rule
    question: How do I disconnect a custom domain from my project?
  phrasing_ops: 9
  slug: appwrite-proxy-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The Locale service allows you to customize your app based on your users' location. 8 operations across 8 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Locale API
  phrasing_intents:
  - id: localeGet
    intent: Detect the user's location from their IP
    question: What country is the current user in, based on their IP address?
  - id: localeListCodes
    intent: List ISO 639-1 locale codes
    question: Which locale codes are supported?
  - id: localeListContinents
    intent: List the world's continents
    question: What continents and continent codes are there?
  - id: localeListCountries
    intent: List all countries
    question: Where can I get a full list of countries for a signup form?
  - id: localeListCountriesEU
    intent: List current EU member countries
    question: Which countries are currently in the European Union?
  - id: localeListCountriesPhones
    intent: List country phone dialing codes
    question: What is the international dialing code for each country?
  - id: localeListCurrencies
    intent: List world currencies
    question: What currencies are supported, with their symbols?
  - id: localeListLanguages
    intent: List world languages
    question: Which languages are listed, with their native names?
  phrasing_ops: 8
  slug: appwrite-locale-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The Affiliates service allows you to share referral codes, track conversions, and apply earned credits. 7 operations across 5 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Affiliates API
  phrasing_intents:
  - id: affiliatesListLinks
    intent: List my affiliate links
    question: Which affiliate links have I created for my Appwrite account?
  - id: affiliatesCreateLink
    intent: Create a shareable affiliate link
    question: How do I get a referral link to share so I earn affiliate rewards?
  - id: affiliatesGetLink
    intent: Get one affiliate link
    question: What are the details of a single affiliate link I own?
  - id: affiliatesDeleteLink
    intent: Delete an affiliate link
    question: If I delete an affiliate link, do the referrals and rewards it already earned stay in my history?
  - id: affiliatesListReferrals
    intent: List referrals from my affiliate links
    question: Who has signed up through my affiliate links so far?
  - id: affiliatesListRewards
    intent: List rewards earned from affiliate conversions
    question: What rewards have I earned from affiliate conversions?
  - id: affiliatesUpdateReward
    intent: Claim an affiliate reward as organization credits
    question: How do I turn a pending affiliate reward into credits for one of my organizations?
  phrasing_ops: 7
  slug: appwrite-affiliates-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The Presences service allows you to track and manage real-time user presence in your project. 6 operations across 3 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Presences API
  phrasing_intents:
  - id: presencesList
    intent: List who is online
    question: Which users are currently online in my app?
  - id: presencesGetUsage
    intent: Get online-user usage metrics
    question: How many users are online right now?
  - id: presencesGet
    intent: Get one presence entry
    question: What is the status of a specific presence entry?
  - id: presencesUpsert
    intent: Set a user's presence status
    question: How do I mark a user as online or away?
  - id: presencesUpdate
    intent: Change fields on an existing presence
    question: Can I change only the status of an existing presence without resending everything?
  - id: presencesDelete
    intent: Delete a presence entry
    question: How do I clear a user's presence when they sign out?
  phrasing_ops: 6
  slug: appwrite-presences-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: Appwrite Cloud regions available to a project, and the regional endpoints they resolve to. 6 operations across 6 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Regions API
  phrasing_intents:
  - id: regionsDeleteCache
    intent: Purge cached platform data across regions
    question: How do I purge a stale cached document from every network region?
  - id: regionsGetDeploymentRuntime
    intent: Get a deployment's runtime info
    question: Which runtime is a given function or site deployment using?
  - id: regionsCreateEvent
    intent: Queue a CloudEvent in a region
    question: How do I queue an event in a region using the CloudEvents format?
  - id: regionsCreateExecution
    intent: Record a function or site execution
    question: How is an execution record logged for a function or site request?
  - id: regionsDeleteProject
    intent: Remove a project from network regions
    question: How do I remove a project from all network regions?
  - id: regionsCreateUsage
    intent: Push usage stats to the usage queue
    question: How are regional usage statistics sent to the stats queue?
  phrasing_ops: 6
  slug: appwrite-regions-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The Webhooks service allows you to manage your project webhooks. 6 operations across 3 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Webhooks API
  phrasing_intents:
  - id: webhooksList
    intent: List the project's webhooks
    question: Which webhooks are configured on my project?
  - id: webhooksCreate
    intent: Create a webhook for project events
    question: How do I get notified at my URL when a document is created or a user signs up?
  - id: webhooksGet
    intent: Get a webhook's configuration
    question: What events and URL is a particular webhook set up with?
  - id: webhooksUpdate
    intent: Update a webhook's URL, events or status
    question: How do I change the URL or events on an existing webhook?
  - id: webhooksDelete
    intent: Delete a webhook
    question: How do I stop a webhook from receiving events permanently?
  - id: webhooksUpdateSecret
    intent: Rotate a webhook's signing secret
    question: How do I rotate the key used to sign webhook payloads?
  phrasing_ops: 6
  slug: appwrite-webhooks-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The Advisor service surfaces actionable reports about your project resources, with CTA descriptors for one-click remediation in the console. 5 operations across 4 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Advisor API
  phrasing_intents:
  - id: advisorListReports
    intent: List the project's analyzer reports
    question: Which analyzer reports has Appwrite Advisor produced for my project?
  - id: advisorGetReport
    intent: Get one analyzer report with its insights
    question: What did a specific analyzer report find, including its nested insights?
  - id: advisorDeleteReport
    intent: Delete an analyzer report
    question: Can I remove an old analyzer report I no longer need?
  - id: advisorListInsights
    intent: List the insights inside one report
    question: What insights did one particular analyzer report produce?
  - id: advisorGetInsight
    intent: Get a single insight from a report
    question: How do I look up the details of one specific advisor insight?
  phrasing_ops: 5
  slug: appwrite-advisor-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The Tokens service allows you to create and manage resource tokens for secure file access. 5 operations across 2 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Tokens API
  phrasing_intents:
  - id: tokensList
    intent: List access tokens issued for a stored file
    question: Which share tokens have already been created for a file in my Appwrite storage bucket?
  - id: tokensCreateFileToken
    intent: Create a shareable access token for a file
    question: How do I generate a token so someone can open a stored file through a URL parameter?
  - id: tokensGet
    intent: Look up a single file token by ID
    question: What are the details and expiry of a specific file token?
  - id: tokensUpdate
    intent: Change the expiry date of a file token
    question: Can I extend the expiry of a file token I already created?
  - id: tokensDelete
    intent: Delete a file access token
    question: How do I stop a file token from granting access by removing it entirely?
  phrasing_ops: 5
  slug: appwrite-tokens-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The Activities service allows you to list and inspect project activity events. 2 operations across 2 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Activities API
  phrasing_intents:
  - id: activitiesListEvents
    intent: List activity events
    question: Where can I see the activity events recorded for my Appwrite account?
  - id: activitiesGetEvent
    intent: Get one activity event
    question: How do I look up the full details of a single activity event by its ID?
  phrasing_ops: 2
  slug: appwrite-activities-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The Notifications service allows you to read and manage your Appwrite Console notifications. 2 operations across 2 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Notifications API
  phrasing_intents:
  - id: notificationsList
    intent: List my console notifications
    question: What notifications do I have waiting in the Appwrite console?
  - id: notificationsUpdate
    intent: Mark a notification read or unread
    question: How do I mark a console notification as read?
  phrasing_ops: 2
  slug: appwrite-notifications-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: Usage reporting for an organization or project across the metered Appwrite resources. 2 operations across 2 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Usage API
  phrasing_intents:
  - id: usageListEvents
    intent: Aggregate usage event metrics over time
    question: What were my top paths by bandwidth over the last 7 days?
  - id: usageListGauges
    intent: Aggregate point-in-time usage gauges
    question: How much file storage is my project holding right now, and how has that snapshot changed?
  phrasing_ops: 2
  slug: appwrite-usage-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The Appwrite Assistant surface used by the Console. 1 operations across 1 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Assistant API
  phrasing_intents:
  - id: assistantChat
    intent: Ask the Appwrite AI assistant a question
    question: Can I ask the Appwrite AI assistant how to set up authentication?
  phrasing_ops: 1
  slug: appwrite-assistant-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: Embedding generation used by VectorsDB similarity search, metered in embedding tokens per model. 1 operations across 1 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Embeddings API
  phrasing_intents:
  - id: embeddingsCreateTextEmbeddings
    intent: Generate vector embeddings for text
    question: How do I turn text into vector embeddings for semantic search?
  phrasing_ops: 1
  slug: appwrite-embeddings-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: Internal growth surface exposed in the published console spec. 1 operations across 1 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Growth API
  phrasing_intents:
  - id: growthCreateInstallation
    intent: Register or update a self-hosted installation
    question: How do I register my self-hosted Appwrite installation with a contact email?
  phrasing_ops: 1
  slug: appwrite-growth-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: Health probe endpoint used to verify connectivity between an SDK and an Appwrite project. 1 operations across 1 paths in the Appwrite 2.0.0 OpenAPI.
  name: Appwrite Ping API
  phrasing_intents:
  - id: pingGet
    intent: Test the SDK connection to the project
    question: Can my SDK actually reach my Appwrite project?
  phrasing_ops: 1
  slug: appwrite-ping-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The OAuth2 service allows you to authorize apps and issue standards-based OAuth2 and OpenID Connect tokens.
  name: Appwrite Oauth2 API
  phrasing_intents:
  - id: oauth2Approve
    intent: Approve a consent grant for an OAuth2 app
    question: How does my consent screen approve an app's authorization request?
  - id: oauth2Authorize
    intent: Start OAuth2 authorization via a GET redirect
    question: What URL do I send a user's browser to so they can sign in to my app with Appwrite OAuth2?
  - id: oauth2AuthorizePost
    intent: Start OAuth2 authorization via a form POST
    question: Can I send the authorization request as a POST body instead of URL parameters?
  - id: oauth2CreateDeviceAuthorization
    intent: Start a device-code sign-in flow
    question: How do I let users sign in on a TV or CLI that has no browser?
  - id: oauth2CreateGrant
    intent: Exchange a device user code for a grant
    question: What happens after a user types the device code shown on their TV?
  - id: oauth2GetGrant
    intent: Get a pending grant for the consent screen
    question: What details should my consent screen show about the access being requested?
  - id: oauth2Logout
    intent: Log out via an OIDC GET redirect
    question: What URL do I redirect to for OpenID Connect logout from my app?
  - id: oauth2LogoutPost
    intent: Log out via an OIDC form POST
    question: Can I end the session with a POST body instead of logout URL parameters?
  phrasing_ops: 14
  slug: appwrite-oauth2-api
- baseURL: https://cloud.appwrite.io/v1
  baseurl_source: declared
  description: The GraphQL API allows you to query and mutate your Appwrite server using GraphQL.
  name: Appwrite Graph QL API
  phrasing_intents:
  - id: graphqlQuery
    intent: Run a GraphQL query
    question: Can I read my Appwrite data with a GraphQL query instead of REST calls?
  - id: graphqlMutation
    intent: Run a GraphQL mutation
    question: How do I change data through a GraphQL mutation?
  phrasing_ops: 2
  slug: appwrite-graph-ql-api
artifact_total: 83
asyncapis:
- description: AsyncAPI specification for the Appwrite Realtime WebSocket API. Appwrite Realtime lets clients subscribe to channels and receive callbacks whenever a subscribed resource changes. Subscriptions are sco
  name: Appwrite Realtime API
  slug: appwrite-asyncapi
- description: ''
  name: Appwrite Webhooks
  slug: appwrite-webhooks
collections:
- collection_type: postman
  name: Appwrite Account API
  slug: postman-appwrite-account-api
- collection_type: postman
  name: Appwrite Account Databases API
  slug: postman-appwrite-databases-api
- collection_type: postman
  name: Appwrite Account Storage API
  slug: postman-appwrite-storage-api
- collection_type: postman
  name: Appwrite Account Users API
  slug: postman-appwrite-users-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Appwrite Account API
  slug: open-appwrite-account-api
- collection_type: open
  name: Appwrite Account Databases API
  slug: open-appwrite-databases-api
- collection_type: open
  name: Appwrite Account Storage API
  slug: open-appwrite-storage-api
- collection_type: open
  name: Appwrite Account Users API
  slug: open-appwrite-users-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/overlays/appwrite-oauth2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appwrite-oauth2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/overlays/appwrite-graphql-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appwrite-graphql-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://appwrite.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://appwrite.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://appwrite.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://appwrite.io/docs/references
- group: start
  title: ''
  type: GettingStarted
  url: https://appwrite.io/docs/quick-starts
- group: company
  title: ''
  type: Blog
  url: https://appwrite.io/blog
- group: operate
  title: ''
  type: Community
  url: https://appwrite.io/community
- group: operate
  title: ''
  type: Support
  url: https://appwrite.io/discord
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/orgs/appwrite/projects
- group: commercial
  title: ''
  type: Pricing
  url: https://appwrite.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.appwrite.io/register
- group: start
  title: ''
  type: Login
  url: https://cloud.appwrite.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appwrite.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appwrite.io/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/appwrite
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/appwrite
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/appwrite/appwrite/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/appwrite/appwrite/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/appwrite/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/appwrite/appwrite/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/appwrite/appwrite/blob/main/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/appwrite/overview
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/packages/appwrite-packages.yml
  title: ''
  type: Packages
  url: packages/appwrite-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/packages/appwrite-packages.yml
  title: ''
  type: SDKs
  url: packages/appwrite-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/cli/appwrite-cli.yml
  title: ''
  type: CLI
  url: cli/appwrite-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/well-known/appwrite-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/appwrite-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/conventions/appwrite-conventions.yml
  title: ''
  type: Conventions
  url: conventions/appwrite-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/errors/appwrite-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/appwrite-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/lifecycle/appwrite-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/appwrite-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://appwrite.io/docs/apis/release-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.appwrite.online/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/changelog/appwrite-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/appwrite-changelog.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/plans/appwrite-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/appwrite-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/rate-limits/appwrite-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/appwrite-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/conformance/appwrite-conformance.yml
  title: ''
  type: Conformance
  url: conformance/appwrite-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://appwrite.io/docs/advanced/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/scopes/appwrite-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/appwrite-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/authentication/appwrite-authentication.yml
  title: ''
  type: Authentication
  url: authentication/appwrite-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/security/appwrite-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appwrite-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/security/appwrite-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/appwrite-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/security/appwrite-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/appwrite-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/appwrite/appwrite/blob/main/SECURITY.md
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/sandbox/appwrite-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/appwrite-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/data-model/appwrite-data-model.yml
  title: ''
  type: DataModel
  url: data-model/appwrite-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/asyncapi/appwrite-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/appwrite-webhooks.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/asyncapi/appwrite-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/appwrite-asyncapi.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/agentic-access/appwrite-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/appwrite-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/finops/appwrite-finops.yml
  title: ''
  type: FinOps
  url: finops/appwrite-finops.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.appwrite.io/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/mcp/appwrite-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/appwrite-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/llms/appwrite-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appwrite-llms.txt
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/appwrite/appwrite
created: '2025-02-17'
description: 'Appwrite is an open-source backend platform for web, mobile and AI applications, shipped both as a self-hostable BSD-3-Clause server and as the managed Appwrite Cloud. One REST API — 1,022 operations across 44 services in the published Appwrite 2.0 OpenAPI, mirrored field-for-field in GraphQL — covers authentication and user management, four database engines (TablesDB, DocumentsDB, VectorsDB and managed PostgreSQL, MySQL and MongoDB), file storage with an S3-compatible surface, serverless Functions, static and SSR Sites hosting, messaging, realtime presence over WebSocket, domains and DNS, backups and a WAF. Appwrite is unusually far forward on the agent layer: it serves an SEP-1649 MCP Server Card and a Domain AI Catalog from its own domain, runs a hosted OAuth-protected MCP endpoint at mcp.appwrite.io alongside a stdio server for self-hosted instances, publishes eleven Agent Skills through a machine-readable discovery index, and gives every documentation, blog and changelog
  page a Markdown twin.'
examples:
- key_count: 10
  name: User Example
  slug: user-example
finops:
- name: Appwrite Finops
  service_category: API
  slug: appwrite-finops
graphqls:
- description: Appwrite exposes its full backend API surface through a GraphQL endpoint that mirrors every REST operation. All services — Account, Databases, Storage, Functions, Teams, Locale, Messaging, and Users —
  name: Appwrite GraphQL API
  slug: appwrite-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/appwrite.png
json_schemas:
- name: User
  property_count: 10
  slug: user
json_structures:
- name: User Structure
  property_count: 0
  slug: user-structure
jsonld:
- class_count: 10
  name: Appwrite Context
  property_count: 0
  slug: appwrite-context
layout: provider
mcp_servers:
- description: ''
  name: Appwrite Remote MCP Server
  slug: appwrite-remote-mcp-server
modified: '2026-09-12'
name: Appwrite
nav: Providers
network: true
overview: 'Appwrite publishes 44 APIs on the [APIs.io](https://apis.io/) network, including Project API, TablesDB API, Account API, and 41 more. Tagged areas include Application, Backend, Mobile, Open Source, and Database.


  The Appwrite catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Appwrite''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 48 more developer resources.'
plans:
- name: Appwrite Plans Pricing
  plan_count: 4
  slug: appwrite-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Appwrite Rate Limits
  slug: appwrite-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Appwrite API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: appwrite-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Appwrite API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: appwrite-jsonschema-spectral-rules
- effective_rule_count: 64
  extends:
  - spectral:oas
  name: Appwrite API Rules
  rule_count: 23
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 14
  slug: appwrite-spectral-rules
scopes:
- name: Appwrite Scopes
  scope_count: 0
  slug: appwrite-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 83.6
  coverage:
    artifact_dirs: 36
    catalog_earned: 74.4
    catalog_earned_first_party: 12.0
    catalog_gap: 40.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 92.1
    contract_governance: 45.5
    contract_quality: 70.8
    developer_ergonomics: 86.9
    discoverability: 75.0
    operational_transparency: 57.9
  open_source:
    applies: true
    score: 100.0
  previous_composite: 83.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 44
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/screenshots/appwrite-2026-06-20T172338.png
security:
- kind: authentication
  name: Appwrite Authentication
  slug: appwrite-authentication
  summary_line: apiKey · 7 schemes
- kind: domain-security
  name: Appwrite Domain Security
  slug: appwrite-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Appwrite Vulnerability Disclosure
  slug: appwrite-vulnerability-disclosure
  summary_line: Hackerone
skill_count: 11
skills:
- name: appwrite-cli
  slug: appwrite-cli
- name: appwrite-dart
  slug: appwrite-dart
- name: appwrite-dotnet
  slug: appwrite-dotnet
- name: appwrite-go
  slug: appwrite-go
- name: appwrite-kotlin
  slug: appwrite-kotlin
- name: appwrite-php
  slug: appwrite-php
- name: appwrite-python
  slug: appwrite-python
- name: appwrite-ruby
  slug: appwrite-ruby
- name: appwrite-rust
  slug: appwrite-rust
- name: appwrite-swift
  slug: appwrite-swift
- name: appwrite-typescript
  slug: appwrite-typescript
slug: appwrite
tags:
- Application
- Backend
- Mobile
- Open Source
- Database
- Storage
- Serverless
- Authentication
- Hosting
- Agents
website: https://appwrite.io/
---
