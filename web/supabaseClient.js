// Example Supabase client for frontend or server-side JS usage.
// Put your keys in environment variables and do NOT commit them.
import { createClient } from '@supabase/supabase-js'

const supabaseUrl = process.env.SUPABASE_URL || 'https://ddobqbscfjqlqcdinsko.supabase.co'
const supabaseKey = process.env.SUPABASE_ANON_KEY || process.env.SUPABASE_KEY
export const supabase = createClient(supabaseUrl, supabaseKey)
