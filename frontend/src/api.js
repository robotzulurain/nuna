// Base configuration
const baseURL = "https://nuna-django.onrender.com/api";

// Helper function for API requests
async function req(url, options = {}) {
  const { params, json, formData, ...fetchOpts } = options;
  let fullURL = baseURL + url;
  
  if (params) {
    const searchParams = new URLSearchParams(params);
    fullURL += "?" + searchParams.toString();
  }
  
  const headers = { ...fetchOpts.headers };
  
  if (json) {
    headers["Content-Type"] = "application/json";
    fetchOpts.body = JSON.stringify(json);
  }
  
  if (formData) {
    fetchOpts.body = formData;
    // Let browser set Content-Type with boundary for FormData
  }
  
  const res = await fetch(fullURL, { ...fetchOpts, headers });
  
  if (!res.ok) {
    throw new Error(`HTTP ${res.status}: ${res.statusText}`);
  }
  
  return res.json();
}

// ---- OPTIONS ----
export const options = () => req("/options");

// ---- SUMMARY ----
export const countsSummary = (params) => req("/summary/counts-summary", { params });
export const timeTrends    = (params) => req("/summary/time-trends",    { params });
export const antibiogram   = (params) => req("/summary/antibiogram",    { params });
export const sexAge        = (params) => req("/summary/sex-age",        { params });

// ---- GEO ----
export const geoFacilities = (params) => req("/geo/facilities", { params });

// ---- REPORTS ----
export const reportSummary        = (params) => req("/reports/summary",         { params });
export const reportFacilityLeague = (params) => req("/reports/facility-league", { params });
export const reportAntibiogram    = (params) => req("/reports/antibiogram",    { params });

// ---- DATA ENTRY ----
export const createEntry = (json) => req("/entry", { method: "POST", json });

export const uploadCSV = (file) => {
  const fd = new FormData();
  fd.append("file", file);
  return req("/upload/csv", { method: "POST", formData: fd });
};

// Default export so older imports still work
const api = {
  options,
  countsSummary,
  timeTrends,
  antibiogram,
  sexAge,
  geoFacilities,
  reportSummary,
  reportFacilityLeague,
  reportAntibiogram,
  createEntry,
  uploadCSV,
};

export default api;
