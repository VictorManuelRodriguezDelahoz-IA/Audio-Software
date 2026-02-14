'use client'

import Link from 'next/link'
import { ArrowRight } from 'lucide-react'

export default function Home() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-recocha-dark p-4 text-white">
      <div className="text-center space-y-6">
        <h1 className="text-5xl font-extrabold tracking-tight">
          Recochapp
        </h1>
        <p className="text-xl text-gray-400 max-w-md">
          Encuentra y organiza recochas de fútbol cerca de ti
        </p>
        <Link
          href="/login"
          className="inline-flex items-center gap-2 rounded-md bg-recocha-neon px-6 py-3 text-sm font-bold text-black hover:bg-white transition-all"
        >
          Entrar a la cancha <ArrowRight className="h-4 w-4" />
        </Link>
      </div>
    </div>
  )
}
