---
aid: bunq
url: https://raw.githubusercontent.com/api-search/banking/main/_apis/bunq/apis.md
apis:
  - aid: bunq:bunq-activity-map-place-api
    name: Bunq Activity Map Place API
    tags: []
    score: 85
    baseURL: https://public-api.sandbox.bunq.com/
    humanURL: https://doc.bunq.com/#/activity-map-place-public
    properties:
      - url: openapi/bunq-activity-map-place-public-itemid-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq Activity Map Place API is a powerful tool that allows developers
      to easily integrate location-based information into their applications.
      With this API, users can access detailed information about various points
      of interest, such as restaurants, shops, and attractions, as well as
      real-time data on traffic and weather conditions. By providing developers
      with access to up-to-date location data, the Bunq Activity Map Place API
      enables them to create more engaging and personalized user experiences.
      Additionally, this API can help businesses improve their marketing
      strategies by better understanding their customers' behavior and
      preferences based on their location data.
  - aid: bunq:bunq-attachment-content-api
    name: Bunq Attachment Content API
    tags:
      - Attachments
      - Content
      - Public
    score: 87
    humanURL: https://doc.bunq.com/#/content
    properties:
      - url: >-
          openapi/bunq-attachment-public-attachment-publicuuid-content-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq Attachment Content API is a tool that allows developers to easily
      manage and access content attached to transactions within the Bunq banking
      system. This API enables users to retrieve, update, and delete various
      types of attachments, such as receipts, invoices, and images, linked to
      their transactions. By using this API, developers can streamline the
      process of organizing and storing transaction-related content, ultimately
      providing a more efficient and user-friendly banking experience for Bunq
      customers.
  - aid: bunq:bunq-attachments-api
    name: Bunq Attachments API
    tags:
      - Attachments
      - Items
      - Users
      - Content
    baseURL: https://public-api.sandbox.bunq.com/
    humanURL: https://doc.bunq.com/#/attachment
    properties:
      - url: openapi/bunq-user-userid-attachment-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      Bunq Attachments API is a tool that allows developers to easily integrate
      file attachments into their applications. With this API, users can upload
      and download various types of files, such as images, documents, and
      videos, directly from their Bunq accounts. This feature enhances the user
      experience by providing a seamless way to manage and access important
      attachments within the Bunq platform. Additionally, the Attachments API
      offers secure and reliable storage for files, ensuring that sensitive
      information remains protected. Overall, the Bunq Attachments API
      simplifies the process of handling attachments for developers and users
      alike, making it a valuable asset for any application utilizing Bunq
      services.
  - aid: bunq:bunq-avatar-api
    name: Bunq Avatar API
    tags:
      - Avatars
      - Items
    score: 86
    humanURL: https://doc.bunq.com/#/avatar
    properties:
      - url: openapi/bunq-avatar--openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq Avatar API is a tool that allows users to easily add personalized
      avatars to their Bunq accounts. By utilizing this API, individuals can
      create unique and customizable avatars that represent their identity
      within the Bunq banking platform. This feature enhances the user
      experience by adding a personal touch to their accounts, making it easier
      to recognize their profile and engage with other users. With the Bunq
      Avatar API, users can upload images, customize their avatars, and easily
      update their profile pictures to reflect their individual style and
      preferences. Overall, the Bunq Avatar API enhances the visual
      representation of user profiles within the Bunq banking platform, making
      it more personalized and user-friendly.
  - aid: bunq:bunq-billing-contract-subscription-api
    name: Bunq Billing Contract Subscription API
    tags:
      - Billing
      - Contracts
      - Subscriptions
      - Users
    humanURL: >-
      https://doc.bunq.com/#/billing-contract-subscription/List_all_BillingContractSubscription_for_User
    properties:
      - url: >-
          openapi/bunq-user-userid-billing-contract-subscription-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq Billing Contract Subscription API is a tool that allows
      businesses to create and manage subscription billing contracts with their
      customers. This API provides businesses with the ability to automate
      recurring billing processes, set up payment schedules, and track customer
      invoices. By using this API, businesses can streamline their subscription
      billing procedures, reduce manual administrative tasks, and improve
      overall efficiency in managing customer contracts. Additionally, the Bunq
      Billing Contract Subscription API integrates seamlessly with existing
      billing systems and provides businesses with real-time updates on payment
      statuses, helping them stay organized and on top of their subscription
      billing operations.
  - aid: bunq:bunq-card-api
    name: Bunq Card API
    tags:
      - Cards
      - Items
      - Users
      - Batches
      - Replace
      - Credit
      - Debit
      - Names
      - Content
      - Exports
      - Statements
      - CSV
      - PDF
      - Generated
    humanURL: https://doc.bunq.com/#/card
    properties:
      - url: openapi/bunq-user-userid-card-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq Card API is a powerful tool that allows developers to integrate
      bunq's innovative banking services directly into their own applications.
      With this API, users can create virtual or physical debit cards, manage
      card settings, and track transactions in real-time. The API provides
      access to customized card designs, instant card activation, and enhanced
      security features such as freezing and unfreezing cards with a single
      click. Additionally, the Bunq Card API enables seamless integration with
      other financial products and services, making it easier for businesses and
      consumers to manage their finances more efficiently and securely.
  - aid: bunq:bunq-certificate-pinning-api
    name: Bunq Certificate Pinning API
    tags:
      - Certificates
      - Pinned
      - Users
      - Items
    score: 292
    humanURL: https://doc.bunq.com/#/certificate-pinned
    properties:
      - url: openapi/bunq-user-userid-certificate-pinned-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq Certificate Pinning API is a security feature that helps protect
      users from man-in-the-middle attacks by verifying the authenticity of the
      server's SSL certificate. By implementing certificate pinning, Bunq
      ensures that the app only communicates with servers that have a specific,
      pre-defined SSL certificate, making it extremely difficult for attackers
      to intercept and manipulate the data being sent and received. This extra
      layer of security gives users peace of mind knowing that their sensitive
      information is being transmitted securely and without the risk of being
      intercepted or tampered with.
  - aid: bunq:bunq-challenge-request-api
    name: Bunq Challenge Request API
    tags:
      - Challenges
      - Items
      - Users
    score: 168
    humanURL: https://doc.bunq.com/#/challenge-request
    properties:
      - url: openapi/bunq-user-userid-challenge-request-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq Challenge Request API is a tool that allows developers to
      facilitate peer-to-peer payments and split bills easily and efficiently.
      With this API, users can create custom challenges and invite friends or
      group members to contribute funds towards a shared goal or expense. The
      API enables seamless communication and tracking of payments, making it
      simple for users to manage shared expenses and track contributions in
      real-time. Additionally, the Bunq Challenge Request API promotes financial
      transparency and accountability among participants, ensuring that everyone
      can easily see who has contributed and how much is still needed to reach
      the desired goal.
  - aid: bunq:bunq-chat-conversation-api
    name: Bunq Chat Conversation API
    tags:
      - Attachments
      - Chat
      - Content
      - Conversations
      - Users
    score: 106
    humanURL: >-
      https://doc.bunq.com/#/content/List_all_Content_for_User_ChatConversation_Attachment
    properties:
      - url: openapi/bunq-user-userid-chat-conversation-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      Bunq Chat Conversation API is a communication tool that allows users to
      have real-time conversations within the Bunq banking app. With this API,
      users can chat with customer support agents, make inquiries about their
      accounts, or engage in discussions with other Bunq users. The Chat
      Conversation API also enables users to receive important notifications and
      updates from Bunq, ensuring that they stay informed about their finances.
      This tool promotes efficient and convenient communication within the
      banking app, enhancing the overall user experience.
  - aid: bunq:bunq-company-api
    name: Bunq Company API
    tags:
      - Companies
      - Users
      - Items
    score: 299
    humanURL: https://doc.bunq.com/#/company
    properties:
      - url: openapi/bunq-user-userid-company-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq Company API is a powerful tool that allows businesses to securely
      access and interact with Bunq's innovative banking platform. With this
      API, companies can easily integrate Bunq's services into their own
      applications and workflows, offering their customers a seamless and
      convenient banking experience. Through the API, businesses can perform a
      wide range of actions, such as initiating payments, checking account
      balances, and managing multiple accounts. This flexibility and
      customization make the Bunq Company API a valuable asset for businesses
      looking to streamline their financial processes and provide a more
      user-friendly banking experience for their customers.
  - aid: bunq:bunq-confirmation-of-funds-api
    name: Bunq Confirmation Of Funds API
    tags:
      - Confirmation
      - Funds
      - Users
    score: 85
    humanURL: >-
      https://doc.bunq.com/#/confirmation-of-funds/CREATE_ConfirmationOfFunds_for_User
    properties:
      - url: openapi/bunq-user-userid-confirmation-of-funds-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      Bunq Confirmation Of Funds API is a service that allows businesses to
      verify the availability of funds in a customer's account before processing
      a payment. This helps to reduce the risk of insufficient funds and
      associated fees, as well as providing peace of mind for both the business
      and the customer. By using this API, businesses can ensure that
      transactions will go through smoothly and efficiently, enhancing the
      overall customer experience. Additionally, the API can help to prevent
      fraud by confirming the legitimacy of the funds being used for a
      transaction. Overall, Bunq Confirmation Of Funds API is a valuable tool
      for businesses looking to streamline their payment processes and improve
      financial security.
  - aid: bunq:bunq-device-api
    name: Bunq Device API
    tags:
      - Device
      - Items
    score: 85
    properties:
      - url: openapi/bunq-device--openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      Bunq Device API is a tool that allows developers to access and interact
      with Bunq's financial services on various devices, such as smartphones,
      tablets, and computers. With this API, developers can create applications
      that enable users to manage their money, make payments, transfer funds,
      and more, all from the convenience of their preferred device. By
      integrating the Bunq Device API into their apps, developers can enhance
      the user experience and provide innovative financial solutions for their
      customers. This API also offers secure authentication and encryption
      protocols to ensure the protection of sensitive financial data.
  - aid: bunq:bunq-device-server-api
    name: Bunq Device Server API
    tags:
      - Device
      - Items
      - Servers
    score: 85
    properties:
      - url: openapi/bunq-device-server--openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq Device Server API is a platform that allows developers to easily
      integrate and communicate with Bunq's banking services. This API enables
      users to securely access their accounts, make payments, and retrieve
      transaction information all through a simple and efficient interface. By
      providing comprehensive documentation and a range of endpoints, the Bunq
      Device Server API streamlines the process of integrating banking
      functionalities into third-party applications, making it easier for
      businesses and individuals to manage their finances seamlessly.
  - aid: bunq:bunq-export-annual-overview-api
    name: Bunq Export Annual Overview API
    tags:
      - Annual
      - Content
      - Exports
      - Overview
      - Users
      - Items
    score: 370
    humanURL: >-
      https://doc.bunq.com/#/content/List_all_Content_for_User_ExportAnnualOverview
    properties:
      - url: openapi/bunq-user-userid-export-annual-overview-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq Export Annual Overview API is a tool that allows users to access
      and download detailed financial information from their Bunq accounts in a
      convenient and streamlined manner. This API provides users with the
      ability to pull their annual financial data, including income, expenses,
      and savings, and export it into various file formats for easy analysis and
      tracking. By utilizing this API, individuals and businesses can gain
      valuable insights into their financial behaviors and make informed
      decisions to improve their financial health and stability.
  - aid: bunq:bunq-fundraiser-profile-api
    name: Bunq Fundraiser Profile API
    tags:
      - Fundraiser
      - Items
      - Profiles
      - Users
    humanURL: >-
      https://doc.bunq.com/#/bunqme-fundraiser-profile/READ_BunqmeFundraiserProfile_for_User
    properties:
      - url: >-
          openapi/bunq-user-userid-bunqme-fundraiser-profile-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq Fundraiser Profile API is a tool that enables organizations and
      individuals to create and manage fundraising campaigns on the Bunq
      platform. With this API, users can easily set up profiles for their
      fundraising efforts, customize them with images and descriptions, and
      track their progress in real-time. The API also provides functionality for
      accepting donations, managing donor information, and generating reporting
      and analytics to help users optimize their campaigns. By using the Bunq
      Fundraiser Profile API, fundraisers can streamline the process of raising
      money for their causes and reach a wider audience of potential donors.
  - aid: bunq:bunq-installation-api
    name: Bunq Installation API
    tags:
      - Installations
      - Items
      - Keys
      - Public
      - Servers
    score: 153
    properties:
      - url: openapi/bunq-installation--openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq Installation API is a tool that allows developers to easily
      integrate Bunq's banking services into their applications. It provides
      access to features such as creating users, setting up accounts, and
      linking payment methods. By using this API, developers can streamline the
      process of incorporating Bunq's services into their products, saving time
      and effort. This API enables seamless communication between the
      application and Bunq's backend systems, ensuring a smooth user experience
      for customers. Overall, the Bunq Installation API simplifies the
      integration of Bunq's banking functionalities, making it easier for
      developers to build innovative financial tools and services.
  - aid: bunq:bunq-installation-installation-server-public-key-api
    name: Bunq Installation Installation Server Public Key API
    tags:
      - Installations
      - Keys
      - Public
      - Servers
    properties:
      - url: >-
          openapi/bunq-installation-installationid-server-public-key-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq Installation Installation Server Public Key API allows users to
      securely register and authenticate their devices with the Bunq
      installation server. By generating a unique public key for each device,
      users can securely communicate with the server, ensuring that their data
      remains private and protected. This API streamlines the process of setting
      up a new device and provides a secure method for users to access their
      Bunq accounts. With strong encryption and authentication measures in
      place, the Installation Installation Server Public Key API helps to
      safeguard user information and maintain the integrity of the Bunq
      platform.
  - aid: bunq:bunq-monetary-account-api
    name: Bunq Monetary Account API
    tags:
      - Accounts
      - Actions
      - Adyen
      - Allocate
      - Attachments
      - Auto
      - Bank
      - Batches
      - Cards
      - Cloud
      - Content
      - Conversions
      - Currencies
      - Customers
      - Definitions
      - Draft
      - Eal
      - Events
      - Exports
      - External
      - Filter
      - Fundraiser
      - Ideal
      - Inquiries
      - Instances
      - Invite
      - Invoices
      - Items
      - Joint
      - Mastercard
      - Merchants
      - Monetary
      - Notes
      - Notifications
      - Payments
      - Quotes
      - Responses
      - Results
      - Savings
      - Schedules
      - Services
      - Share
      - Statements
      - Switch
      - Tabs
      - Text
      - Transactions
      - URL
      - Users
      - Whitelist
    baseURL: https://public-api.sandbox.bunq.com/
    humanURL: https://doc.bunq.com/#/monetary-account
    properties:
      - url: openapi/bunq-user-userid-monetary-account-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq Monetary Account API is a powerful tool that allows developers to
      seamlessly integrate Bunq's revolutionary banking services into their own
      applications. With this API, developers can easily create and manage
      monetary accounts, send and receive payments, and access account
      information in real-time. The API also provides advanced features such as
      setting up automatic transfers, tracking expenses, and monitoring account
      balances. By leveraging the Bunq Monetary Account API, developers can
      provide their users with a seamless and convenient banking experience, all
      while ensuring the highest levels of security and reliability.
  - aid: bunq:bunq-oauth-client-api
    name: Bunq Oauth Client API
    tags:
      - Callback
      - Clients
      - Items
      - OAuth
      - URL
      - Users
    score: 696
    humanURL: https://doc.bunq.com/#/
    properties:
      - url: openapi/bunq-user-userid-oauth-client-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq Oauth Client API is a service that allows developers to easily
      integrate the Bunq banking platform into their applications. By utilizing
      OAuth authentication, users can securely connect their bank accounts to
      third-party apps for seamless access to their financial information. The
      API provides endpoints for managing user sessions, retrieving account
      information, making payments, and more. With the Bunq Oauth Client API,
      developers can create innovative financial tools and services that enhance
      the banking experience for users.
  - aid: bunq:bunq-payment-service-provider-credential-api
    name: Bunq Payment Service Provider Credential API
    tags:
      - Credentials
      - Er
      - Items
      - Payments
      - Prov
      - Providers
      - Services
    properties:
      - url: openapi/bunq-payment-service-provider-credential--openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq Payment Service Provider Credential API allows businesses to
      securely link their payment service provider accounts with their Bunq
      accounts, enabling seamless and efficient payment processing. This API
      provides businesses with a secure method of accessing and managing their
      payment service provider credentials, allowing for easy integration with
      their existing payment infrastructure. With the Bunq Payment Service
      Provider Credential API, businesses can streamline their payment
      processes, reduce administrative burden, and enhance overall efficiency in
      managing their payment transactions. By providing a simple and reliable
      way to manage payment credentials, this API empowers businesses to
      optimize their payment operations and drive growth.
  - aid: bunq:bunq-registry-import-splitwise-csv-api
    name: Bunq Registry Import Splitwise Csv API
    tags: []
    properties:
      - url: openapi/bunq-registry-import-splitwise-csv--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://apis.apievangelist.com/store/bunq-registry-import-splitwise-csv-api
        type: Documentation
    description: >-
      The Bunq Registry Import Splitwise Csv API is a tool that allows users to
      easily import their Splitwise transactions into their Bunq account. With
      this API, users can conveniently transfer data from their Splitwise
      account to their Bunq account, eliminating the need for manual data entry.
      This helps users keep track of their expenses and finances in a more
      organized and efficient manner. Additionally, the API enables users to
      split expenses and manage their shared expenses with friends or roommates
      seamlessly. Overall, the Bunq Registry Import Splitwise Csv API simplifies
      the process of managing finances and ensures accurate and up-to-date
      transaction records.
  - aid: bunq:bunq-sandbox-user-company-api
    name: Bunq Sandbox User Company API
    tags: []
    properties:
      - url: openapi/bunq-sandbox-user-company--openapi-original.yml
        type: OpenAPI
      - url: https://beta.doc.bunq.com/basics/sandbox
        type: Documentation
    description: >-
      The Bunq Sandbox User Company API is a tool that allows developers to
      easily create and manage sample company accounts within the Bunq financial
      platform for testing purposes. This API provides developers with the
      ability to simulate various company profiles, including employees, bank
      accounts, transactions, and more, in order to test and debug their
      applications in a controlled environment. By using the Sandbox User
      Company API, developers can ensure that their integrations with Bunq's
      services perform as expected before deploying them to production,
      ultimately improving the reliability and security of their financial
      applications.
  - aid: bunq:bunq-sandbox-user-person-api
    name: Bunq Sandbox User Person API
    tags: []
    properties:
      - url: openapi/bunq-sandbox-user-person--openapi-original.yml
        type: OpenAPI
      - url: https://beta.doc.bunq.com/basics/sandbox
        type: Documentation
    description: >-
      The Bunq Sandbox User Person API is a tool designed to allow developers to
      create and manipulate virtual user accounts within the Bunq banking
      system. By using this API, developers can simulate various user scenarios,
      such as opening new accounts, making transactions, and managing funds, all
      within a secure and controlled testing environment. This functionality is
      particularly useful for testing and developing new features or
      applications that interact with the Bunq banking platform, without needing
      to access real user data. Overall, the Sandbox User Person API provides a
      valuable resource for developers looking to integrate with Bunq and ensure
      the functionality and security of their applications.
  - aid: bunq:bunq-server-error-api
    name: Bunq Server Error API
    tags: []
    properties:
      - url: openapi/bunq-server-error--openapi-original.yml
        type: OpenAPI
      - url: https://beta.doc.bunq.com/basics/errors
        type: Documentation
    description: >-
      Bunq Server Error API is a tool designed to help developers troubleshoot
      issues and debug server errors within the Bunq banking platform. This API
      provides detailed information about server errors, including error codes,
      error messages, and possible solutions. By integrating this API into their
      applications, developers can quickly identify and resolve server errors to
      ensure a smooth and seamless user experience. Additionally, Bunq Server
      Error API allows developers to track and monitor server errors over time,
      helping them to proactively address any recurring issues and optimize the
      performance of their applications.
  - aid: bunq:bunq-session-item-api
    name: Bunq Session Item API
    tags: []
    properties:
      - url: openapi/bunq-session-itemid--openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq Session Item API is a tool that allows developers to securely
      manage and access user-specific data within the Bunq banking platform.
      This API enables users to create and modify session items, which are
      essentially temporary containers for storing extra information related to
      a user's session. By utilizing this API, developers can enhance the
      functionality of their applications by storing and retrieving additional
      data that is relevant to a particular user session. This can help to
      improve the user experience and provide more personalized features for
      Bunq users. Ultimately, the Bunq Session Item API makes it easier for
      developers to create more dynamic and interactive applications within the
      Bunq ecosystem.
  - aid: bunq:bunq-session-server-api
    name: Bunq Session Server API
    tags: []
    properties:
      - url: openapi/bunq-session-server--openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq Session Server API is a powerful tool that allows developers to
      easily manage user sessions within the Bunq platform. By utilizing this
      API, developers can create and manage user sessions, including logins,
      access tokens, and session cookies. This makes it easier for users to
      securely access their accounts and perform transactions within the Bunq
      app. The Session Server API also provides tools for managing session
      expiration, refreshing access tokens, and monitoring user activity.
      Overall, the Bunq Session Server API simplifies the process of managing
      user sessions and increases the security and efficiency of the Bunq
      platform.
  - aid: bunq:bunq-transaction-categories-api
    name: Bunq Transaction Categories API
    tags:
      - Additional
      - Categories
      - Information
      - Transactions
      - Users
      - Defined
    score: 156
    baseURL: https://public-api.sandbox.bunq.com/
    humanURL: https://doc.bunq.com/#/additional-transaction-information-category
    properties:
      - url: >-
          openapi/bunq-user-userid-additional-transaction-information-category-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq Transaction Categories API is a tool that allows users to easily
      categorize their transactions based on various criteria. This API assists
      in sorting transactions into specific categories such as groceries,
      dining, entertainment, and more, making it easier for users to track and
      manage their spending habits. By integrating this API into their
      platforms, users can get a better understanding of where their money is
      being spent and make more informed financial decisions. Overall, the Bunq
      Transaction Categories API helps users maintain a clear overview of their
      finances and stay on top of their budgeting goals.
  - aid: bunq:bunq-user-company-item-api
    name: Bunq User Company Item API
    tags: []
    properties:
      - url: openapi/bunq-user-company-itemid--openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Company Item API is a tool that allows companies to access
      and manage their user data and company information within the Bunq
      platform. With this API, users can view and update their account details,
      transaction history, and other relevant information related to their
      company's finances. This enables companies to easily track their financial
      activities, monitor account balances, and seamlessly integrate their
      banking data with other business systems. The Bunq User Company Item API
      provides a secure and efficient way for companies to stay organized and
      informed about their financial status in real-time.
  - aid: bunq:bunq-user-company-user-company-name-api
    name: Bunq User Company User Company Name API
    tags:
      - Companies
      - Names
      - Users
    properties:
      - url: openapi/bunq-user-company-user-companyid-name-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Company User Company Name API is a powerful tool that allows
      businesses to seamlessly integrate Bunq's banking services into their own
      applications and systems. With this API, companies can access a wide range
      of features, including real-time payment processing, account management,
      and transaction tracking. By leveraging the Bunq User Company User Company
      Name API, businesses can provide their customers with a streamlined and
      efficient banking experience, while also gaining valuable insights into
      their financial operations. This API helps companies to improve their
      overall service offerings and drive growth by offering innovative banking
      solutions.
  - aid: bunq:bunq-user-credential-password-ip-api
    name: Bunq User Credential Password Ip API
    tags:
      - Credentials
      - IP
      - Items
      - Password
      - Users
    score: 484
    properties:
      - url: openapi/bunq-user-userid-credential-password-ip-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Credential Password Ip API is a tool that allows Bunq users
      to securely access their accounts and perform various banking transactions
      using their credentials, password, and IP address. This API provides a
      secure authentication method for users to log in to their Bunq accounts
      while also verifying their identity through their password and IP address.
      By implementing this API, Bunq can ensure that only authorized users are
      able to access their accounts and carry out financial activities,
      enhancing the overall security and protection of user data and funds.
  - aid: bunq:bunq-user-currency-cloud-beneficiary-api
    name: Bunq User Currency Cloud Beneficiary API
    tags: []
    score: 294
    properties:
      - url: >-
          openapi/bunq-user-userid-currency-cloud-beneficiary-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Currency Cloud Beneficiary API is a tool designed to
      streamline the process of sending money internationally. By connecting
      with Currency Cloud, users are able to easily create and manage
      beneficiary accounts for cross-border transactions. This API allows Bunq
      users to securely store recipient information, including bank account
      details and contact information, and automate the transfer of funds to
      these beneficiaries when needed. With the Currency Cloud Beneficiary API,
      users can reduce the time and effort required to make international
      payments, ultimately providing a more efficient and convenient solution
      for managing cross-border transactions.
  - aid: bunq:bunq-user-event-api
    name: Bunq User Event API
    tags:
      - Events
      - Items
      - Users
    score: 164
    properties:
      - url: openapi/bunq-user-userid-event-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Event API is a tool that allows Bunq users to access and
      manage real-time data about their account activities and events. This API
      enables users to retrieve information such as transaction history, account
      balances, and notifications in a quick and efficient manner. With the Bunq
      User Event API, users have the ability to stay informed about their
      financial transactions and make more informed decisions about their money
      management. Overall, this API provides users with a seamless and
      convenient way to access and monitor their account information.
  - aid: bunq:bunq-user-feature-announcement-api
    name: Bunq User Feature Announcement API
    tags:
      - Announcement
      - Feature
      - Items
      - Users
    score: 95
    properties:
      - url: openapi/bunq-user-userid-feature-announcement-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Feature Announcement API is a tool that allows developers to
      stay up-to-date with the latest features and updates released by Bunq, a
      mobile banking platform. With this API, developers can access information
      about new features, bug fixes, and enhancements as soon as they are
      announced. This enables them to integrate these updates into their own
      applications quickly and efficiently, ensuring that their users have
      access to the most current and innovative banking solutions. By utilizing
      the Bunq User Feature Announcement API, developers can enhance the user
      experience and stay ahead of the competition in the ever-evolving world of
      digital banking.
  - aid: bunq:bunq-user-insight-preference-date-api
    name: Bunq User Insight Preference Date API
    tags:
      - Dates
      - Insights
      - Preferences
      - Users
    score: 86
    properties:
      - url: openapi/bunq-user-userid-insight-preference-date-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Insight Preference Date API is a tool that allows users to
      access and manipulate their personal data preferences within the Bunq app.
      With this API, users can customize their preferences and settings to
      tailor their banking experience to their individual needs. This includes
      setting preferences for notifications, alerts, and other relevant
      information that the user may want to receive. The API also enables users
      to easily manage and update their preferences in real-time, providing a
      seamless and user-friendly way to interact with their financial data.
      Overall, the Bunq User Insight Preference Date API is a powerful tool that
      empowers users to take control of their banking experience and personalize
      it to suit their preferences.
  - aid: bunq:bunq-user-insights-api
    name: Bunq User Insights API
    tags:
      - Insights
      - Users
      - Search
    score: 154
    properties:
      - url: openapi/bunq-user-userid-insights-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      Bunq User Insights API is a powerful tool that provides businesses with
      detailed information about their customers' behavior and preferences
      within the Bunq finance app. By leveraging this API, businesses can access
      data such as transaction history, spending habits, and account balances of
      their users, allowing them to gain valuable insights that can be used to
      tailor their products and services to better meet the needs of their
      customers. This data-driven approach can help businesses improve customer
      satisfaction, increase engagement, and drive growth by making more
      informed decisions based on real-time data. Overall, the Bunq User
      Insights API enables businesses to better understand and serve their
      customers, ultimately leading to a more successful and sustainable
      business.
  - aid: bunq:bunq-user-invoice-api
    name: Bunq User Invoice API
    tags:
      - Invoices
      - Users
      - Items
      - Content
      - PDF
    score: 241
    properties:
      - url: openapi/bunq-user-userid-invoice-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Invoice API is a tool that allows users to easily create and
      manage invoices within the Bunq platform. With this API, users can
      generate professional and customizable invoices, track payment statuses,
      and send reminders to clients for outstanding payments. Additionally, the
      API provides real-time updates on invoice activities, making it easy for
      users to stay on top of their financial transactions. With the Bunq User
      Invoice API, users can streamline their invoicing process, reduce manual
      input, and ensure prompt payment for their goods and services.
  - aid: bunq:bunq-user-item-api
    name: Bunq User Item API
    tags: []
    properties:
      - url: openapi/bunq-user-itemid--openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      Bunq User Item API is a tool that allows users to access and manage items
      within their Bunq account. With this API, users can view, create, update,
      and delete various items such as transactions, payments, and account
      information. The API provides a user-friendly interface that makes it easy
      for individuals to interact with their account data and make any necessary
      adjustments. Additionally, the Bunq User Item API offers a secure and
      reliable way for users to manage their finances and stay on top of their
      banking needs.
  - aid: bunq:bunq-user-legal-name-api
    name: Bunq User Legal Name API
    tags:
      - Legal
      - Names
      - Users
    score: 86
    properties:
      - url: openapi/bunq-user-userid-legal-name-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Legal Name API is a tool that allows developers to access
      the legal names of Bunq users for verification and identification
      purposes. By utilizing this API, developers can securely retrieve and
      verify the true identity of Bunq users, ensuring that their transactions
      and account activities are conducted with accurate and up-to-date
      information. This API enhances the security and trustworthiness of the
      Bunq platform, helping to prevent fraud and unauthorized access to user
      accounts. Overall, the Bunq User Legal Name API provides a valuable
      resource for developers seeking to enhance the security and reliability of
      their Bunq integrations.
  - aid: bunq:bunq-user-limit-api
    name: Bunq User Limit API
    tags:
      - Limits
      - Users
    score: 86
    properties:
      - url: openapi/bunq-user-userid-limit-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Limit API is a tool that allows users to set and manage
      limits on various transactions within their Bunq account. This includes
      setting limits on daily spending, maximum transaction amounts, ATM
      withdrawals, and more. The API gives users the ability to customize their
      limits based on their individual needs and preferences, providing greater
      control over their finances and enhancing security measures. By utilizing
      this API, Bunq users can easily adjust their limits in real-time and
      monitor their transactions to ensure they stay within their desired
      boundaries.
  - aid: bunq:bunq-user-monetary-account-bank-api
    name: Bunq User Monetary Account Bank API
    tags:
      - Accounts
      - Bank
      - Monetary
      - Users
      - Items
    score: 299
    properties:
      - url: openapi/bunq-user-userid-monetary-account-bank-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Monetary Account Bank API is a financial tool that provides
      users with access to their Bunq monetary account information through a
      programming interface. This API allows users to retrieve details about
      their account balance, transaction history, and other financial data
      securely. By integrating this API into their applications, developers can
      create personalized financial management solutions for Bunq users,
      streamlining their banking experience and helping them make informed
      financial decisions. Overall, the Bunq User Monetary Account Bank API
      enhances the functionality of the Bunq banking platform by providing users
      with convenient access to their account information and empowering
      developers to build innovative financial applications.
  - aid: bunq:bunq-user-monetary-account-card-api
    name: Bunq User Monetary Account Card API
    tags:
      - Accounts
      - Cards
      - Items
      - Monetary
      - Users
    score: 236
    properties:
      - url: openapi/bunq-user-userid-monetary-account-card-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Monetary Account Card API provides users with the ability to
      manage and maintain their monetary account cards within the Bunq
      ecosystem. With this API, users can create and manage virtual and physical
      cards, assign spending limits and restrictions, track transactions in
      real-time, and receive notifications for any card activities. Users can
      also block or unblock cards, view card balances and transaction history,
      and facilitate seamless payments and transfers. The API streamlines the
      process of managing monetary account cards, offering users greater control
      and flexibility over their finances.
  - aid: bunq:bunq-user-monetary-account-external-api
    name: Bunq User Monetary Account External API
    tags:
      - Accounts
      - External
      - Monetary
      - Users
      - Items
      - Savings
    score: 580
    humanURL: https://doc.bunq.com/#/monetary-account-external
    properties:
      - url: >-
          openapi/bunq-user-userid-monetary-account-external-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Monetary Account External API is a tool that allows users to
      access and manage their monetary accounts on the Bunq platform through
      external applications. With this API, users can perform a variety of
      functions such as checking their account balances, making payments,
      transferring funds, and viewing transaction histories. This API provides a
      convenient and efficient way for users to interact with their Bunq
      monetary accounts and integrates seamlessly with external applications to
      enhance the overall user experience.
  - aid: bunq:bunq-user-monetary-account-joint-api
    name: Bunq User Monetary Account Joint API
    tags:
      - Accounts
      - Joint
      - Monetary
      - Users
      - Items
    score: 300
    properties:
      - url: openapi/bunq-user-userid-monetary-account-joint-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Monetary Account Joint API is a financial tool that allows
      users to easily manage and monitor joint monetary accounts. With this API,
      users can track transactions, set spending limits, and receive
      notifications for account activity. This tool also enables users to
      securely share access to their joint accounts with other authorized
      individuals, making it easier to collaborate on managing shared finances.
      Additionally, the Bunq User Monetary Account Joint API streamlines the
      process of making payments, transfers, and other financial tasks within a
      joint account, providing an efficient and user-friendly solution for
      shared financial management.
  - aid: bunq:bunq-user-monetary-account-savings-api
    name: Bunq User Monetary Account Savings API
    tags:
      - Accounts
      - Monetary
      - Savings
      - Users
      - Items
    score: 301
    properties:
      - url: openapi/bunq-user-userid-monetary-account-savings-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Monetary Account Savings API is a financial tool that allows
      users to easily save and manage their money. With this API, users can set
      up different savings goals, track their progress, and automate transfers
      to their savings account. This API also provides insights into spending
      habits and suggests ways to save more effectively. By using the Bunq User
      Monetary Account Savings API, users can take control of their finances and
      work towards achieving their financial goals with ease.
  - aid: bunq:bunq-user-notification-filter-email-api
    name: Bunq User Notification Filter Email API
    tags:
      - Emails
      - Filter
      - Notifications
      - Users
    properties:
      - url: >-
          openapi/bunq-user-userid-notification-filter-email-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      Bunq User Notification Filter Email API is a tool that allows users to
      filter and customize the emails they receive from Bunq, a mobile banking
      app. This API enables users to set up specific criteria and rules to only
      receive notifications about certain transactions, account updates, or
      other relevant information. By using this API, users can tailor their
      email notifications to suit their preferences and ensure they only receive
      the most important and relevant updates from Bunq. This helps users manage
      their inbox more effectively and stay informed about important banking
      activities without being overwhelmed by unnecessary notifications.
  - aid: bunq:bunq-user-notification-filter-failure-api
    name: Bunq User Notification Filter Failure API
    tags:
      - Failure
      - Filter
      - Notifications
      - Users
    properties:
      - url: >-
          openapi/bunq-user-userid-notification-filter-failure-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Notification Filter Failure API is a tool that allows users
      to filter notifications based on specific parameters set by the user. This
      API helps users manage the overwhelming amount of notifications they
      receive by allowing them to customize and prioritize which notifications
      they want to see. If there is a failure in the notification filter, this
      API will alert the user so they can address the issue and ensure they are
      receiving the notifications that are most important to them.Overall, the
      Bunq User Notification Filter Failure API provides a more efficient and
      personalized notification system for users to better manage their Bunq
      account.
  - aid: bunq:bunq-user-notification-filter-push-api
    name: Bunq User Notification Filter Push API
    tags:
      - Filter
      - Notifications
      - Users
    properties:
      - url: openapi/bunq-user-userid-notification-filter-push-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Notification Filter Push API is a tool that allows users to
      customize and filter the notifications they receive from the Bunq banking
      platform. By utilizing this API, users can set specific criteria for the
      types of notifications they want to receive, such as transaction alerts,
      account balance updates, or payment reminders. This level of customization
      helps users stay informed about their finances in a way that is most
      relevant and useful to them. Additionally, the push notification feature
      ensures that users are promptly notified of important updates and changes
      to their accounts, leading to a more streamlined and efficient banking
      experience.
  - aid: bunq:bunq-user-notification-filter-url-api
    name: Bunq User Notification Filter Url API
    tags:
      - Filter
      - Notifications
      - URL
      - Users
    properties:
      - url: openapi/bunq-user-userid-notification-filter-url-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Notification Filter Url API allows users to customize and
      filter the notifications they receive from the Bunq app. By providing a
      URL endpoint, users can specify the criteria for which notifications they
      want to receive, such as specifying a certain transaction amount or type
      of transaction. This API empowers users to tailor their notification
      preferences to their specific needs, ensuring they only receive the most
      relevant and important updates, leading to a more streamlined and
      personalized user experience.
  - aid: bunq:bunq-user-payment-auto-allocate-api
    name: Bunq User Payment Auto Allocate API
    tags:
      - Allocate
      - Auto
      - Payments
      - Users
    properties:
      - url: openapi/bunq-user-userid-payment-auto-allocate-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Payment Auto Allocate API is a feature offered by the Bunq
      banking platform that allows users to automate the allocation of incoming
      payments to specific budget categories or savings goals. This API
      streamlines the process of managing finances by automatically distributing
      funds based on predetermined rules set by the user. By setting up rules
      such as allocating a portion of each paycheck to savings, or distributing
      funds to different expense categories, users can effortlessly stay on
      track with their financial goals without having to manually manage each
      transaction. Overall, Bunq User Payment Auto Allocate API simplifies the
      budgeting process and helps users maintain control over their finances
      with ease.
  - aid: bunq:bunq-user-payment-service-provider-draft-payment-api
    name: Bunq User Payment Service Provider Draft Payment API
    tags:
      - Draft
      - Er
      - Payments
      - Prov
      - Providers
      - Services
      - Users
      - Items
    properties:
      - url: >-
          openapi/bunq-user-userid-payment-service-provider-draft-payment-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Payment Service Provider Draft Payment API is a solution
      that enables users to create drafts for payments within the Bunq banking
      platform. This allows users to easily initiate payments and send them for
      approval before they are finalized. With this API, users can draft
      payments for various purposes, such as paying bills, sending money to
      friends or family, or making purchases online. The API streamlines the
      payment process, making it more efficient and convenient for users to
      manage their finances through the Bunq platform.
  - aid: bunq:bunq-user-payment-service-provider-issuer-transaction-api
    name: Bunq User Payment Service Provider Issuer Transaction API
    tags:
      - Er
      - Issuer
      - Payments
      - Prov
      - Providers
      - Services
      - Transactions
      - Users
      - Items
    properties:
      - url: >-
          openapi/bunq-user-userid-payment-service-provider-issuer-transaction-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Payment Service Provider Issuer Transaction API is a
      powerful tool that allows users to access and manage their payment
      transactions through the Bunq platform. With this API, users can easily
      view detailed information about their transactions, including the amount,
      date, and recipient. Additionally, users can initiate new transactions,
      such as making payments or transferring funds, directly through the API.
      This streamlined process simplifies the user experience and provides a
      convenient way to track and manage financial transactions. Overall, the
      Bunq User Payment Service Provider Issuer Transaction API enhances the
      user's ability to stay on top of their finances and make quick, secure
      transactions.
  - aid: bunq:bunq-user-payment-service-provider-item-api
    name: Bunq User Payment Service Provider Item API
    tags: []
    properties:
      - url: >-
          openapi/bunq-user-payment-service-provider-itemid--openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Payment Service Provider Item API allows users to access and
      manage their payment service provider items through the Bunq platform.
      This API enables users to view details of their items, update payment
      provider data, and monitor transaction activity. By integrating with the
      API, businesses and individuals can streamline their payment processes,
      ensuring that their payment provider items are always up-to-date and
      accurate. With secure and efficient access to their payment service
      provider items, users can easily track payments, reconcile accounts, and
      manage their financial transactions with ease.
  - aid: bunq:bunq-user-person-item-api
    name: Bunq User Person Item API
    tags: []
    properties:
      - url: openapi/bunq-user-person-itemid--openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Person Item API is a tool designed to allow users to
      interact with and manage their personal financial data within the Bunq
      platform. This API enables users to access and retrieve information about
      their accounts, transactions, and other financial activities, as well as
      perform various actions such as making payments, transferring funds, and
      managing standing orders. By connecting to the Bunq User Person Item API,
      users can seamlessly integrate their financial data into third-party
      applications and tools, ultimately providing a more streamlined and
      efficient way to manage their finances.
  - aid: bunq:bunq-user-registry-api
    name: Bunq User Registry API
    tags:
      - Registries
      - Settlements
      - Users
      - Items
    properties:
      - url: openapi/bunq-user-userid-registry-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Registry API is a tool that allows developers to access and
      manage user information within the Bunq platform. With this API, users can
      easily retrieve details such as contact information, account numbers, and
      transaction history for each individual user. This streamlined access to
      user data enables developers to create personalized and efficient user
      experiences, as well as securely authenticate users and verify their
      identity. The Bunq User Registry API is a powerful tool for businesses
      looking to enhance the efficiency and security of their user management
      processes.
  - aid: bunq:bunq-user-schedule-api
    name: Bunq User Schedule API
    tags:
      - Schedules
      - Users
    properties:
      - url: openapi/bunq-user-userid-schedule-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Schedule API allows developers to create and manage
      scheduled transactions for Bunq users. This API enables users to set up
      automated payments, transfers, or other financial activities to occur at
      specified times and frequencies. With this functionality, users can easily
      plan and organize their finances, ensuring that important transactions are
      carried out on time without the need for manual intervention. This API
      enhances the user experience by providing a convenient and efficient way
      to automate recurring financial tasks within the Bunq ecosystem.
  - aid: bunq:bunq-user-share-invite-monetary-account-response-api
    name: Bunq User Share Invite Monetary Account Response API
    tags:
      - Accounts
      - Invite
      - Items
      - Monetary
      - Share
      - Users
    properties:
      - url: >-
          openapi/bunq-user-userid-share-invite-monetary-account-response-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Share Invite Monetary Account Response API is a tool that
      allows users to share and invite others to join their Bunq account, while
      also facilitating monetary transactions. With this API, users can easily
      send and receive money, split bills, and make payments to family and
      friends. Additionally, users can invite others to join their Bunq account,
      enabling them to access shared funds and make transactions within the
      shared account. This API streamlines the process of managing finances with
      others, making it simple and efficient to collaborate on expenses and
      payments.
  - aid: bunq:bunq-user-token-qr-request-eal-api
    name: Bunq User Token Qr Request Eal API
    tags:
      - Ideal
      - Tokens
      - Users
    properties:
      - url: openapi/bunq-user-userid-token-qr-request-ideal-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Token Qr Request Eal API is a feature that allows users to
      securely generate and request a one-time QR code token for authentication
      purposes. This token is used to access sensitive information or perform
      transactions within the Bunq platform. The API ensures that only
      authorized users can access their accounts by requiring them to scan the
      QR code with their mobile device. This additional layer of security helps
      to prevent unauthorized access and protect user data from potential cyber
      threats. Overall, the Bunq User Token Qr Request Eal API enhances the
      security measures of the Bunq platform and provides users with peace of
      mind when managing their finances online.
  - aid: bunq:bunq-user-token-qr-request-sofort-api
    name: Bunq User Token Qr Request Sofort API
    tags:
      - Tokens
      - Users
    properties:
      - url: openapi/bunq-user-userid-token-qr-request-sofort-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Token Qr Request Sofort API is a tool that allows users to
      generate QR codes for requesting payment tokens in real-time. This API
      enables users to quickly and easily create secure payment requests using a
      unique token system. By simply scanning the QR code with their mobile
      device, customers can instantly authorize transactions and complete
      payments without the need for manual input or data entry. This streamlined
      process not only enhances user experience but also ensures a high level of
      security and efficiency for businesses and consumers alike.
  - aid: bunq:bunq-user-transferwise-currency-api
    name: Bunq User Transferwise Currency API
    tags:
      - Currencies
      - Transferwise
      - Users
    properties:
      - url: openapi/bunq-user-userid-transferwise-currency-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Transferwise Currency API allows users to easily transfer
      money between their Bunq account and their Transferwise account in
      different currencies. This API simplifies the process of exchanging money
      and ensures that users can quickly and securely transfer funds without the
      need for traditional bank transfers. With this API, users can seamlessly
      manage their finances across multiple accounts and currencies, making it
      easier to transact globally and save on expensive currency exchange fees.
  - aid: bunq:bunq-user-transferwise-quote-api
    name: Bunq User Transferwise Quote API
    tags:
      - Quotes
      - Transferwise
      - Users
      - Items
      - Temporary
      - Recipient
      - Requirements
      - Transfers
    properties:
      - url: openapi/bunq-user-userid-transferwise-quote-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Transferwise Quote API is a tool that allows Bunq users to
      obtain real-time quotes for currency exchange rates and fees when
      transferring money through Transferwise. By utilizing this API, users can
      easily compare rates and fees across different currencies, helping them to
      make more informed decisions when sending money internationally. This API
      provides users with transparency and clarity on the cost of their
      transfers, allowing them to save money and time on their cross-border
      transactions. Overall, the Bunq User Transferwise Quote API simplifies the
      process of sending money abroad for Bunq users, making it easier for them
      to manage their finances efficiently.
  - aid: bunq:bunq-user-transferwise-user-api
    name: Bunq User Transferwise User API
    tags:
      - Transferwise
      - Users
    properties:
      - url: openapi/bunq-user-userid-transferwise-user-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Transferwise User API allows Bunq users to seamlessly
      transfer money using Transferwise's platform. This API facilitates
      convenient, fast, and secure international money transfers for Bunq
      account holders, with the added benefit of Transferwise's competitive
      exchange rates and low fees. Users can easily initiate transfers, track
      their status, and manage their transactions directly within the Bunq app,
      making cross-border payments simpler and more efficient. Additionally, the
      integration of Transferwise's innovative technology ensures that transfers
      are executed quickly and accurately, providing a seamless user experience
      for both Bunq and Transferwise customers.
  - aid: bunq:bunq-user-tree-progress-api
    name: Bunq User Tree Progress API
    tags:
      - Progress
      - Trees
      - Users
    properties:
      - url: openapi/bunq-user-userid-tree-progress-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Tree Progress API is a tool that allows users to track their
      progress and activity within the Bunq app. By providing access to a
      comprehensive overview of their financial behavior and transactions, users
      can gain valuable insights into their spending habits, saving goals, and
      overall financial health. This API also enables users to set personalized
      goals and benchmarks, monitor their progress, and receive real-time
      notifications to help them stay on track. With the Bunq User Tree Progress
      API, users can take control of their financial journey and make informed
      decisions to improve their financial well-being.
  - aid: bunq:bunq-user-whitelist-sdd-api
    name: Bunq User Whitelist Sdd API
    tags:
      - Items
      - Users
      - Whitelist
      - Recurring
    properties:
      - url: openapi/bunq-user-userid-whitelist-sdd-openapi-original.yml
        type: OpenAPI
      - url: https://doc.bunq.com/
        type: Documentation
    description: >-
      The Bunq User Whitelist Sdd API allows users to securely manage and
      control their SEPA Direct Debit mandates. With this API, users can create
      and maintain whitelists of authorized payers, ensuring that only approved
      entities are able to initiate direct debit transactions. This feature
      helps to protect users from unauthorized or fraudulent transactions,
      giving them peace of mind as they conduct their banking activities. By
      using the User Whitelist Sdd API, Bunq users can enjoy an added layer of
      security and control over their financial transactions.
name: Bunq
tags:
  - Banking
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
score: 1805
access: 3rd-Party
common:
  - url: https://developer.bunq.com/en/
    type: Portal
  - url: https://doc.bunq.com/#/authentication
    type: Authentication
  - url: https://doc.bunq.com/#/errors
    type: Errors
  - url: https://doc.bunq.com/#/headers
    type: Headers
  - url: https://example.com
    type: Type
  - url: https://doc.bunq.com/#/callbacks
    type: Callbacks
  - url: https://doc.bunq.com/#/pagination
    type: Pagination
  - url: https://beta.doc.bunq.com/basics/changelog
    type: Change Log
  - url: https://status.bunq.com/
    type: Status
  - url: https://github.com/bunq
    type: GitHub Organization
  - url: https://github.com/bunq/postman/
    type: Postman Collections
  - url: https://beta.doc.bunq.com/basics/sandbox
    type: Sandbox
  - url: https://medium.com/bunq-developers-corner
    type: Blog
  - url: https://beta.doc.bunq.com/other/faq
    type: FAQ
  - url: >-
      https://assets-global.website-files.com/63b43f001c7774d38d5f3a2d/63b43f001c7774ee815f41aa_20200805_terms_bunq_API_EN.pdf
    type: Terms of Service
  - url: https://www.bunq.com/
    name: bunq | bank of The Free
    type: Website
    description: 'null'
  - url: https://www.bunq.com/blog
    name: Blog | bunq
    type: Blog
    description: 'null'
  - url: https://www.bunq.com/about
    name: About Us | bunq
    type: About
    description: 'null'
  - url: https://www.bunq.com/security
    name: Security | bunq
    type: Security
    description: 'null'
  - url: https://press.bunq.com/
    name: bunq Newsroom
    type: PressReleases
    description: 'null'
  - url: https://static.bunq.com/framer/documents/Pricing-en-EU.pdf
    name: none
    type: Pricing
    description: 'null'
  - url: https://www.bunq.com/help
    name: Help | bunq
    type: Support
    description: 'null'
  - url: https://together.bunq.com/t/faq
    name: Frequently Asked Questions - bunq Together
    type: FAQ
    description: 'null'
  - url: https://www.bunq.com/documents/terms-conditions
    name: Terms & Conditions - Documents | bunq
    type: TermsOfService
    description: 'null'
  - url: https://www.bunq.com/documents/privacy
    name: Privacy Policy | bunq
    type: PrivacyPolicy
    description: 'null'
  - url: https://web.bunq.com/
    name: bunq Web
    type: Login
    description: 'null'
  - url: https://web.bunq.com/signup?language=en_US&tracker_token=dqvbt6
    name: bunq Web
    type: SignUp
    description: 'null'
created: 2023/11/13
modified: '2025-01-05'
position: Consuming
description: >-
  Bunq is a digital bank that offers innovative banking solutions to its
  customers. With Bunq, users can easily manage their finances through their
  mobile app, which gives them full control over their accounts and
  transactions. Bunq also provides various features such as instant payments,
  budgeting tools, and savings goals to help users better manage their money.
  Additionally, Bunq is known for its commitment to sustainability and
  transparency, as they offer a green card that plants a tree for every 100
  spent, and they do not invest in industries that harm the environment.
  Overall, Bunq strives to redefine the banking experience by providing a
  user-friendly platform that puts the needs of its customers first.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.16'

---