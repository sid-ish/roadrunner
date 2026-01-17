export default function VideoPlayer({ src }) {
  return <video controls className="w-full" src={src} />;
}
