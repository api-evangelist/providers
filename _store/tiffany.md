---
aid: tiffany
url: https://raw.githubusercontent.com/api-evangelist/tiffany/refs/heads/main/apis.yml
name: Tiffany & Co.
description: Tiffany & Co. is a global luxury jeweler and specialty retailer founded in 1837, acquired by LVMH in 2021. The company designs, manufactures, and sells jewelry, watches, fragrances, and accessories under the Tiffany brand across over 300 stores worldwide and a robust e-commerce platform. Tiffany operates a B2B corporate gifting platform and retail e-commerce site with back-end order management integration. The company does not currently offer a public developer API or partner developer program; integration is available through their corporate gifting portal and select enterprise channels.
image: https://www.tiffany.com/favicon.ico
tags:
  - Corporate Gifting
  - E-Commerce
  - Jewelry
  - Luxury Retail
  - Watches
created: '2024'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: tiffany:tiffany-ecommerce
    name: Tiffany & Co. E-Commerce Platform
    description: Tiffany & Co.'s direct-to-consumer e-commerce platform at tiffany.com, enabling online browsing, customization, and purchase of jewelry, watches, accessories, and home items. The platform supports product discovery by category, material, price, and occasion. No public API is documented; retail integration is through the website and mobile app.
    image: https://www.tiffany.com/favicon.ico
    humanURL: https://www.tiffany.com
    baseURL: https://www.tiffany.com
    tags:
      - E-Commerce
      - Jewelry
      - Luxury Retail
      - Retail
    properties:
      - type: Website
        url: https://www.tiffany.com
      - type: Mobile App
        url: https://www.tiffany.com/accessibility/
  - aid: tiffany:tiffany-corporate-gifting
    name: Tiffany & Co. Corporate Gifting Platform
    description: Tiffany & Co.'s B2B corporate gifting and recognition program platform, providing procurement and delivery of corporate gifts and recognition items. The platform includes order management system integration, advanced reporting, analytics, and e-catalog management. Enterprise clients may access order and catalog data through select B2B integrations.
    image: https://www.tiffany.com/favicon.ico
    humanURL: https://www.tiffany.com/en-us/gifts/corporate-gifting/
    baseURL: https://www.tiffany.com/en-us/gifts/corporate-gifting/
    tags:
      - B2B
      - Corporate Gifting
      - Enterprise
      - Jewelry
      - Recognition
    properties:
      - type: Documentation
        url: https://www.tiffany.com/en-us/gifts/corporate-gifting/
common:
  - type: Website
    url: https://www.tiffany.com
  - type: Corporate Gifting
    url: https://www.tiffany.com/en-us/gifts/corporate-gifting/
  - type: Privacy Policy
    url: https://www.tiffany.com/accessibility/privacy-policy/
  - type: Terms of Service
    url: https://www.tiffany.com/accessibility/terms-and-conditions/
  - type: Twitter
    url: https://twitter.com/tiffanyandco
  - type: Instagram
    url: https://www.instagram.com/tiffanyandco/
  - type: Facebook
    url: https://www.facebook.com/tiffanyandco/
  - type: LinkedIn
    url: https://www.linkedin.com/company/tiffany-co/
  - type: JSON-LD
    url: json-ld/tiffany-context.jsonld
  - type: JSONSchema
    url: json-schema/tiffany-product-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
