import Image from 'next/image'
import Hello from '@/components/main'
export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center ">
      <Hello />
    </main>
  )
}
