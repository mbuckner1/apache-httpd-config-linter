# Rules Reference

This section details every rule the linter checks, including security rationale and configuration examples.

---

## 1. AllowOverride All

- **Rule ID:** DIR_ALLOWOVERRIDE_ALL
- **Severity:** HIGH
- **Description:** The `AllowOverride All` directive allows all .htaccess overrides, potentially leading to insecure configurations and privilege escalation.
- **Recommendation:** Use `AllowOverride None` and move necessary configuration into the main config file.
- **Example:**
    ```apache
    <Directory "/var/www/html">
        AllowOverride None
    </Directory>
    ```

---

## 2. Options Indexes

- **Rule ID:** DIR_OPTIONS_INDEXES
- **Severity:** MEDIUM
- **Description:** Enabling `Indexes` in the `Options` directive exposes directory listings, leaking sensitive files.
- **Recommendation:** Remove `Indexes` from `Options`.
- **Example:**
    ```apache
    Options -Indexes +FollowSymLinks
    ```

---

## 3. Missing ServerTokens

- **Rule ID:** GLOBAL_SERVERTOKENS_MISSING
- **Severity:** MEDIUM
- **Description:** If `ServerTokens` is not set, Apache may reveal version information in HTTP headers, aiding attackers.
- **Recommendation:** Set `ServerTokens Prod` to limit information disclosure.
- **Example:**
    ```apache
    ServerTokens Prod
    ```

---

## 4. mod_status Enabled

- **Rule ID:** MOD_STATUS_EXPOSED
- **Severity:** LOW
- **Description:** The `mod_status` module exposes server status information. If not access-restricted, it may leak sensitive operational data.
- **Recommendation:** Restrict access to `/server-status` or disable `mod_status` in production.
- **Example:**
    ```apache
    <Location "/server-status">
        SetHandler server-status
        Require ip 127.0.0.1
    </Location>
    ```

---

## More Rules

For the full list of rules, see the source code or contribute your own checks.

---
