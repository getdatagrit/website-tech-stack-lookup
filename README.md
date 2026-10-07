# Website Tech Stack Lookup - Technology Detector

Detect the technology stack of any list of domains: CMS, ecommerce, analytics, CDN, frameworks with versions, plus mail provider, SPF and DMARC.

[![Run on Apify](https://img.shields.io/badge/Run%20on-Apify-0f9f74)](https://apify.com/datagrit/website-tech-stack-lookup) [![Docs](https://img.shields.io/badge/docs-getdatagrit.github.io-0e1726)](https://getdatagrit.github.io/website-tech-stack-lookup/)

**from $14.00 per 1,000 results + $10 per run (pay per result; the rate depends on your Apify plan).** Export as JSON, CSV or Excel, call it through the API, or schedule it on Apify.

## What it does

Website Tech Stack Lookup tells you which technologies a list of websites runs on: CMS, ecommerce platform, analytics, tag manager, CDN, hosting, web server, JavaScript framework, marketing and chat tools, payment providers and hundreds more, with the version when the site exposes it, a confidence score and the evidence behind every detection. It also reads the public DNS of each domain to report the **mail provider (MX)**, the **SPF record** with the email services it authorises, the **DMARC policy** and the DNS provider. Paste domains or URLs, run, and export JSON, CSV or Excel, or call it from the Apify API, n8n, Make or an AI agent through MCP.

## Quick start

1. Open [Website Tech Stack Lookup - Technology Detector on Apify Store](https://apify.com/datagrit/website-tech-stack-lookup) and click **Try for free**.
2. Fill in the input form (or paste the JSON below) and run it.
3. Download the dataset, or fetch it from the API.

```json
{
  "domains": [
    "shopify.com",
    "wordpress.org",
    "hubspot.com",
    "stripe.com",
    "vercel.com",
    "bbc.co.uk",
    "allbirds.com",
    "techcrunch.com",
    "webflow.com",
    "joomla.org",
    "github.com",
    "apify.com"
  ]
}
```

## Input

| Field | Type | What it does |
|---|---|---|
| `domains` | array | Domains (shopify.com), hostnames (www.bbc.co.uk) or full URLs (https://example.com/pricing), one per line. A bare domain is fetched at https://domain/, then https://www.domain/ and http://domain/ if the first address does not answer; a full URL is fetched exactly as given. Duplicates (with or without www, http or https) are merged, and entries that are not domains or http(s) URLs are listed in the run status. Leave empty to get a free example for two well-known sites. |
| `categories` | array | Optional. Limit the technologies list (technologies, technologyNames, technologyCategories, technologyCount) to these categories. The summary columns (cms, ecommerce, analytics, mailProvider and the rest) are always filled from every detected technology. Categories: A/B testing, Accessibility, Advertising, Affiliate, Analytics, Blog, Build tool, Business software, CDN, CMS, CRM, Captcha, Comments, Cookie consent, Customer data platform, Customer support, DNS provider, Documentation, Ecommerce, Email marketing, Email provider, Email service, Feature flags, Font service, Forms, Forum, Headless CMS, Hosting, Image CDN, JavaScript CDN, JavaScript framework, JavaScript library, LMS, Live chat, Loyalty & referrals, Maps, Marketing automation, Monitoring, Operating system, PaaS, Payment, Personalization, Popups, Product adoption, Product search, Programming language, Push notifications, Reviews, SEO, Scheduling, Security, Session replay, Social, Static site generator, Subscriptions, Tag manager, Translation, UI framework, Video, Web framework, Web server, Website builder. |
| `requireTechnologies` | array | Optional lead filter. Return (and charge for) a site only when it uses at least one of these technologies, for example Shopify, WooCommerce or HubSpot. Names are matched case-insensitively against the technology names in the output; unknown names are listed in the run status. Sites that do not match are skipped without charge. Unreachable sites still get a free row with found: false. |
| `followRedirects` | boolean | Follow HTTP redirects (and one meta refresh) to the final page and analyze that page. Turn off to analyze only the first response; a redirect is then returned with its status code and redirectLocation. |
| `includeDns` | boolean | Look up MX, TXT (SPF and verification records), DMARC, NS, CNAME and A/PTR records of each domain to report the mail provider, SPF and DMARC, the DNS provider and services that verified the domain. Turn off for faster runs when you need only the website stack. |
| `maxConcurrency` | integer | How many sites are analyzed at the same time. Every site is a different server, so a higher value mostly speeds up long lists. |
| `requestTimeoutSecs` | integer | How long to wait for each page before trying the next address or reporting the site as unreachable (reason timeout). |
| `proxyConfiguration` | object | Optional proxy for the page requests. Most sites answer without one; sites behind strict bot protection may block data center addresses and are then reported with found: false and reason blocked-by-bot-protection. DNS lookups do not use the proxy. |

## Output

| Field | Type | Description |
|---|---|---|
| `input` | string | The entry exactly as it appeared in your list. |
| `domain` | string | Registrable domain of the entry (public suffix aware, so www.bbc.co.uk gives bbc.co.uk). DNS checks (MX, SPF, DMARC, NS) run on this domain. |
| `url` | string | First URL requested for this entry. For a bare domain this is https://domain/; when it did not answer, the fallbacks https://www.domain/ and http://domain/ were tried. |
| `host` | string | Hostname from your entry, lowercased and converted to ASCII (punycode). |
| `finalUrl` | string | URL of the page that was analyzed, after redirects (when Follow redirects is on). |
| `statusCode` | integer | HTTP status code of the analyzed response. Null when the site did not answer at all. |
| `redirectLocation` | string | Where the site redirects to, filled only when Follow redirects is off and the first response is a redirect. |
| `title` | string | Text of the <title> tag of the analyzed page. |
| `language` | string | Page language from the <html lang> attribute, falling back to the Content-Language header and og:locale. |
| `technologyCount` | integer | Number of technologies in the technologies list (after the Technology categories filter). |
| `technologyNames` | string | Comma-separated names of the listed technologies, highest confidence first. |
| `technologyCategories` | string | Comma-separated distinct categories of the listed technologies. |
| `technologies` | array | Every detected technology with its category, version when the site exposes one, confidence from 0 to 100 and up to three pieces of evidence (header, meta tag, script URL, cookie name, HTML snippet, DNS record, or the technology that implies it). |
| `cms` | string | Detected CMS, website builder, headless CMS or blog platform, with version when known. Always filled from all detected technologies, whatever the categories filter. |
| `ecommerce` | string | Detected ecommerce platform(s), with version when known. |
| `analytics` | string | Detected analytics tools. For Google Analytics the version is GA4 or UA (Universal Analytics). |
| `tagManager` | string | Detected tag managers. |
| `cdn` | string | Detected content delivery network in front of the site. |
| `hosting` | string | Detected hosting provider or platform (from response headers, CNAME, A and PTR records). |
| `webServer` | string | Detected web server or reverse proxy, with version when the Server header exposes it. |
| `jsFramework` | string | Detected front-end frameworks. |
| `programmingLanguage` | string | Detected server-side language, with version when a header exposes it. |
| `marketingAutomation` | string | Detected marketing automation and email marketing tools (from page scripts and SPF includes). |
| `liveChat` | string | Detected live chat and customer support tools. |
| `payment` | string | Detected payment providers (from checkout scripts and domain verification records). |
| `dnsProvider` | string | DNS hosting provider from the NS records of the domain. |
| `emailServices` | string | Transactional email services authorised in the SPF record. |
| `mailProvider` | string | Provider that receives mail for the domain, from its MX records. "Other" means MX records exist but point to a provider the Actor does not recognise (see mxRecords). Null when the domain has no MX record or DNS was not checked. |
| `mxRecords` | string | Up to five MX hosts, lowest priority value first. |
| `hasSpf` | boolean | True when the domain publishes a v=spf1 TXT record, false when it does not, null when DNS was not checked or did not answer. |
| `spfRecord` | string | The SPF record text (first 500 characters). |
| `hasDmarc` | boolean | True when _dmarc.<domain> publishes a v=DMARC1 record, false when it does not, null when DNS was not checked or did not answer. |
| `dmarcPolicy` | string | Policy (p=) of the DMARC record: none, quarantine or reject. |
| `dnsChecked` | boolean | True when the MX, TXT, DMARC and NS lookups all answered (an empty answer counts). False when some lookup failed, so a null mail field may mean "unknown". Null when DNS checks were turned off or the site row is found: false. |
| `htmlAnalyzed` | boolean | True when the response was an HTML page and its markup, scripts and meta tags were analyzed; false when only headers, cookies and DNS were available. |
| `errorReason` | string | Why a row has found: false: dns-not-found, dns-error, connection-refused, connection-reset, timeout, tls-error, host-unreachable, too-many-redirects, fetch-error, http-error, rate-limited, blocked-by-bot-protection, or no-matching-sites for the single status row when Only sites using any of these technologies matched nothing. |
| `errorMessage` | string | Details of the error, such as the HTTP status or the network error. |
| `found` | boolean | True for an analyzed site (charged). False for a site that could not be analyzed and for the status row; these rows are free. |
| `scrapedAt` | string | ISO 8601 time of the check. |
| `sourceUrl` | string | URL of the analyzed page (same as finalUrl), or the requested URL when the site did not answer. |

Sample record:

```json
{
  "input": "shopify.com",
  "domain": "bbc.co.uk",
  "url": "https://shopify.com/",
  "host": "shopify.com",
  "finalUrl": "https://www.shopify.com/",
  "statusCode": 200,
  "redirectLocation": null,
  "title": "Shopify: The All-in-One Commerce Platform",
  "language": "en-US",
  "technologyCount": 18,
  "technologyNames": "Shopify, Cloudflare, Google Workspace, React",
  "technologyCategories": "Ecommerce, CDN, Email provider, JavaScript framework",
  "technologies": [
    {
      "name": "WordPress",
      "category": "CMS",
      "version": "6.8.2",
      "confidence": 100,
      "evidence": [
        "meta generator: WordPress 6.8.2",
        "script https://example.com/wp-includes/js/jquery/jquery.min.js?ver=3.7.1"
      ]
    }
  ],
  "cms": "WordPress 6.8.2",
  "ecommerce": "Shopify",
  "analytics": "Google Analytics GA4, Hotjar",
  "tagManager": "Google Tag Manager",
  "cdn": "Cloudflare",
  "hosting": "Vercel",
  "webServer": "Nginx 1.24.0",
  "jsFramework": "Next.js, React",
  "programmingLanguage": "PHP 8.2.12",
  "marketingAutomation": "HubSpot, Klaviyo",
  "liveChat": "Intercom",
  "payment": "Stripe, PayPal",
  "dnsProvider": "Cloudflare DNS",
  "emailServices": "SendGrid, Amazon SES",
  "mailProvider": "Google Workspace",
  "mxRecords": "aspmx.l.google.com, alt1.aspmx.l.google.com",
  "hasSpf": true,
  "spfRecord": "v=spf1 include:_spf.google.com ~all",
  "hasDmarc": true,
  "dmarcPolicy": "reject",
  "dnsChecked": true,
  "htmlAnalyzed": true,
  "errorReason": null,
  "errorMessage": null,
  "found": true,
  "scrapedAt": "2026-10-01T08:00:00.000Z",
  "sourceUrl": "https://www.shopify.com/"
}
```

## Call it from code

Runnable examples are in [`examples/`](examples). Replace `YOUR_APIFY_TOKEN` with the token from your Apify account settings.

```bash
curl -X POST "https://api.apify.com/v2/acts/datagrit~website-tech-stack-lookup/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"domains":["shopify.com","wordpress.org","hubspot.com","stripe.com","vercel.com","bbc.co.uk","allbirds.com","techcrunch.com","webflow.com","joomla.org","github.com","apify.com"]}'
```


## More from datagrit

- [Domain WHOIS RDAP Lookup - DNS, MX & Expiry](https://github.com/getdatagrit/domain-whois-rdap-lookup) - Bulk domain lookup: official RDAP (WHOIS) registration, expiry and availability plus DNS, mail provider, SPF/DMARC and hosting ASN, with expiry and registrar filters.
- [TED Contract Expiry Radar - Recompete Leads](https://github.com/getdatagrit/ted-contract-expiry-radar) - Find EU public contracts approaching expiry from TED award notices: incumbent, buyer, value, end date and renewal options.
- [UK Contract Expiry Radar - Recompete Leads](https://github.com/getdatagrit/uk-contract-expiry-radar) - UK public contracts ending soon with incumbent supplier, buyer, value and contact - recompete leads from Contracts Finder award notices.
- [French Company Finder - Sirene Financials](https://github.com/getdatagrit/french-company-finder) - French company lead lists from Sirene screened by net result and revenue, with net margin, size, matching establishment and optional directors.
- [IRS 990 Nonprofit Officers and Compensation](https://github.com/getdatagrit/irs-990-officer-compensation) - Named officers, directors and key employees with pay, hours and titles from IRS e-filed 990, 990-EZ and 990-PF returns.

All Actors: [https://getdatagrit.github.io/](https://getdatagrit.github.io/) · [Apify Store](https://apify.com/datagrit)

---

This repository holds documentation and usage examples. Questions, bug reports and feature requests: use the **Issues** tab of the Actor page on [Apify Store](https://apify.com/datagrit/website-tech-stack-lookup). Examples are MIT licensed.
