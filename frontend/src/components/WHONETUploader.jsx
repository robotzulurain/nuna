import { useState } from "react";
import { uploadCSV } from "../api.js";

export default function WHONETUploader({ onUpload }) {
  const [uploading, setUploading] = useState(false);
  const [message, setMessage] = useState("");

  const handleUpload = async (blob, filename) => {
    setUploading(true);
    setMessage("");
    try {
      // Create a File object from the blob
      const file = new File([blob], filename, { type: "text/csv" });
      const result = await uploadCSV(file);
      setMessage(`Upload successful! ${result.row_count} rows processed.`);
      onUpload?.(result);
    } catch (err) {
      setMessage(`Upload failed: ${err.message}`);
    } finally {
      setUploading(false);
    }
  };

  // ... rest of your WHONETUploader component logic
  return (
    <div>
      {/* Your WHONET uploader UI */}
      <p>WHONET Uploader Component - Using API function</p>
    </div>
  );
}
