import { useState } from "react";
import { uploadCSV } from "../api.js";

export default function BulkUpload({ onUpload }) {
  const [uploading, setUploading] = useState(false);
  const [message, setMessage] = useState("");

  const handleUpload = async (file) => {
    if (!file) return;
    setUploading(true);
    setMessage("");
    try {
      const result = await uploadCSV(file);
      setMessage(`Upload successful! ${result.row_count} rows processed.`);
      onUpload?.(result);
    } catch (err) {
      setMessage(`Upload failed: ${err.message}`);
    } finally {
      setUploading(false);
    }
  };

  return (
    <div>
      <input
        type="file"
        accept=".csv"
        onChange={(e) => handleUpload(e.target.files[0])}
        disabled={uploading}
      />
      {message && <p>{message}</p>}
    </div>
  );
}
